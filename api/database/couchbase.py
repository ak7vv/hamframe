# module contains couchbase related code

from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator
from couchbase.bucket import Bucket

def check_couchbase(couchbase):
    return

# https://www.couchbase.com/blog/how-implement-document-versioning-couchbase/
# reimplemented in Python

# Create a new document

def version_document(key, value):
    # Step 1: Get the current version of the document
    try:
        current_doc = collection.get(key).content_as[str]
    except:
        current_doc = None
    
    if current_doc:
        # Step 2: Increment the version number
        try:
            version = collection.binary().increment(f"{key}_version", 1, initial=1)
        except:
            version = 1

        version_key = f"{key}::v{version}"

        # Step 3: Create the version with the new key
        try:
            collection.upsert(version_key, current_doc)
        except Exception as e:
            print(f"Cannot save version {version} for key {key} – Error: {e}")

    # Step 4: Save the document current version
    collection.upsert(key, value)

# Delete all versions of a document

def delete_document(key):
    # Step 1: Get the current version of the document
    try:
        current_doc = collection.get(key).content_as[str]
    except:
        current_doc = None

    if current_doc:
        # Step 2: Get the highest version number
        try:
            version = int(collection.get(f"{key}_version").content_as[str])
        except:
            version = 0

        # Step 3: Delete all versions
        for i in range(1, version + 1):
            version_key = f"{key}::v{i}"
            collection.remove(version_key)

        # Step 4: Delete the version counter
        collection.remove(f"{key}_version")

    # Step 5: Delete the current version
    collection.remove(key)
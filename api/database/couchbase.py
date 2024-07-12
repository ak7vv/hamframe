from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.bucket import Bucket
from couchbase.exceptions import CouchbaseException

def check_couchbase(couchbase_param):
    """
    Check if the Couchbase configuration endpoint is alive and return a handle if successful.
    
    :param couchbase_param: dictionary of the Couchbase endpoint (.endpoint), username (.username) and password (.password), and bucket (.bucket) to check
    :return: (status_code, couchbase) tuple where status_code is boolean for the check success, and bucket is the Couchbase bucket if successful
    """
# check if we have a valid couchbase cluster connection and a valid bucket

    status_code = None
    try:
        cluster = Cluster(couchbase_param.endpoint,
                            ClusterOptions(
                                PasswordAuthenticator(
                                    couchbase_param.username,
                                    couchbase_param.password)))

        bucket = cluster.bucket(couchbase_param.bucket)
        
        bucket.on_connect()

        return True, bucket

    except CouchbaseException as e:
        return False, None
    
    

# Inspired by https://www.couchbase.com/blog/how-implement-document-versioning-couchbase/
# reimplemented in Python

# Create a new document

def version_document(couchbase_collection, key, value):
# we are being provided a valid couchbase_collection handle, a key, 
# and a value to populate the key with

    # Step 1: Get the current version of the document
    try:
        current_doc = couchbase_collection.get(key).content_as[str]
    except:
        current_doc = None
    
    if current_doc:
        # Step 2: Increment the version number
        try:
            version = couchbase_collection.binary().increment(f"{key}_version", 1, initial=1)
        except:
            version = 1

        version_key = f"{key}::v{version}"

        # Step 3: Create the version with the new key
        try:
            couchbase_collection.upsert(version_key, current_doc)
        except Exception as e:
            print(f"Cannot save version {version} for key {key} – Error: {e}")

    # Step 4: Save the document current version
    couchbase_collection.upsert(key, value)

# Delete all versions of a document

def delete_document(couchbase_collection, key):
# we are being provided a valid couchbase_collection handle, a key, 
# and a value to populate the key with

    # Step 1: Get the current version of the document
    try:
        current_doc = couchbase_collection.get(key).content_as[str]
    except:
        current_doc = None

    if current_doc:
        # Step 2: Get the highest version number
        try:
            version = int(couchbase_collection.get(f"{key}_version").content_as[str])
        except:
            version = 0

        # Step 3: Delete all versions
        for i in range(1, version + 1):
            version_key = f"{key}::v{i}"
            couchbase_collection.remove(version_key)

        # Step 4: Delete the version counter
        couchbase_collection.remove(f"{key}_version")

    # Step 5: Delete the current version
    couchbase_collection.remove(key)
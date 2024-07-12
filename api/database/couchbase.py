from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.exceptions import CouchbaseException

def check_couchbase(couchbase_param):
    """
    Check if the Couchbase configuration endpoint is alive, if bucket exists, and return a handle to bucket if successful.
    If no bucket is specified, check 'default' bucket.
    
    :param couchbase_param: dictionary of the Couchbase endpoint (.endpoint), username (.username) and password (.password), and bucket (.bucket) to check
    :return: (status_code, couchbase) tuple where status_code is boolean for the check success, and bucket is the Couchbase bucket if successful
    """

    # did we get all required params?
    if ( not couchbase_param.endpoint or 
         not couchbase_param.username or 
         not couchbase_param.password or 
         not couchbase_param.bucket ):
        return False, None

    # check if what we were given actually works    
    try:
        couchbase_cluster = Cluster(couchbase_param.endpoint,
                            ClusterOptions(
                                PasswordAuthenticator(
                                    couchbase_param.username,
                                    couchbase_param.password)))

        couchbase_bucket = couchbase_cluster.bucket(couchbase_param.bucket)
        
        couchbase_bucket.on_connect()

        return True, couchbase_bucket

    except CouchbaseException as e:
        return False, None
    
    



def version_document(couchbase_collection, key, value):
    """
    Version a Couchbase document with a new value

    :param couchbase_collection: handle for a valid Couchbase collection
    :return: boolean on whether op was successful (FIXME https://github.com/ckuhtz/hamframe/issues/3)
    """
    # Inspired by https://www.couchbase.com/blog/how-implement-document-versioning-couchbase/
    # reimplemented in Python

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
    """
    Delete all versions of a Couchbase document

    :param couchbase_collection: handle for a valid Couchbase collection
    :return: boolean on whether op was successful (FIXME https://github.com/ckuhtz/hamframe/issues/4)
    """

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
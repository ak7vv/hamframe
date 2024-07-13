import redis
import urllib.parse

def check_conf_server(host_param):
    """
    Check if the Redis configuration endpoint is alive and return a handle if successful.
    
    :param host_param: the Redis endpoint (.e.g, 'redis://localhost')
    :param db: the name of the Redis database to connect to
    :return: (status_code, r) tuple where status_code is boolean for the check success, and r is the Redis handle if successful
    """

    redissplit = urllib.parse.urlsplit('//' + host_param) # split parameter into .hostname and .port
    if redissplit.port:
            redisport = redissplit.port
    else:
            redisport = 6379
    try:
        r = redis.StrictRedis(host=redissplit.hostname, port=redisport, decode_responses=True )
        if r.ping():
            return True, r
        return False, None
    
    except redis.ConnectionError:
        return False, None


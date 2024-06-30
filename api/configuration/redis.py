# module contains redis related code
# check_conf_server() takes what we hope to be parts of a URL for Redis, constructs valid connection
# parameters, checks the connection and returns a boolean as well as a Redis handle if successful. 

import redis
import urllib.parse

def check_conf_server(host_param, db):
    if not db:
          return False, None
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


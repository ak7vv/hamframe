# module provides functions to import toml and export toml from a configuration dict
# logger : defines which logging instance should be used
# instance_name : prescriptive info as to which instance this configuration table should apply to
# table_name : prescriptive info as to what table should be written in redis
# toml_dict : dictionary with toml data for table table_name



import sys
import json



def toml_import(logger, toml_file)
    
    logger.debug("> " + sys._getframe().f_code.co_name + "()")
    
    # dump the dict we're supposed to write to kv store as JSON
    dict_as_json = json.dumps(str(toml_dict))
    logger.debug(dict_as_json)

    # write meta data to redis
    
    logger.debug("< " + sys._getframe().f_code.co_name + "()")
    return toml_dict



def toml_export(logger, redis, instance_name, table_name):

    logger.debug("> " + sys._getframe().f_code.co_name + "()")
    
    # initialize toml_dict dict since it doesn't exist here

    toml_dict = {'instance' : instance_name, 'table' : table_name }

    # dump the dict retrieved from kv store as JSON
    logger.debug(json.dumps(str(toml_dict)))

    logger.debug("< " + sys._getframe().f_code.co_name + "()")
    return toml_dict

# module provides functions to import toml to redis and export redis to toml
#
# logger : defines which logging instance should be used
# instance_name : prescriptive info as to which instance this configuration table should apply to
# table_name : prescriptive info as to what table should be written in redis
# toml_dict : dictionary with toml data for table table_name



def toml_import(logger, instance_name, table_name, **toml_dict):
    logger.info("toml_import() start")
    logger.debug("instance_name: " + instance_name)
    logger.debug("table_name: " + table_name)
    logger.debug("toml_dict: " + toml_dict)

    logger.debug("toml_import() complete")
    return



def toml_export(logger, instance_name, table_name):
    toml_dict = {}

    logger.info("toml_export() start")
    logger.debug("instance_name: " + instance_name)
    logger.debug("table_name: " + table_name)

    # report what we retrieved and return the dict
    logger.debug("toml_dict: " + str(toml_dict))
    logger.debug("toml_import() complete")
    return toml_dict

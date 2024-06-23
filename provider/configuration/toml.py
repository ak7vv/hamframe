# module provides functions to import toml to redis and export redis to toml
#
# logger : defines which logging instance should be used
# instance_name : prescriptive info as to which instance this configuration table should apply to
# table_name : prescriptive info as to what table should be written in redis
#

def toml_import(logger, instance_name, table_name):
    logger.info("toml_import()")
    logger.debug("table_name: ", table_name)
    return

def toml_export(logger, instance_name, table_name):
    logger.info("toml_import()")
    logger.debug("table_name: ", table_name)

    return

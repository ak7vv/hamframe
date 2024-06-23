# module provides functions to import toml to redis and export redis to toml
#
# logger : defines which logging instance should be used
# instance_name : prescriptive info as to which instance this configuration table should apply to
# table_name : prescriptive info as to what table should be written in redis
# toml_dict : dictionary with toml data for table table_name



def toml_import(logger, instance_name, table_name, **toml_dict):
    logger.info("toml_import()")
    logger.debug("instance_name: ", instance_name)
    logger.debug("table_name: ", table_name)
    logger.debug("toml_dict: ", toml_dict)

    return



def toml_export(logger, instance_name, table_name):
    logger.info("toml_import()")
    logger.debug("instance_name: ", instance_name)
    logger.debug("table_name: ", table_name)

    logger.debug("toml_dict: ", toml_dict)
    return toml_dict

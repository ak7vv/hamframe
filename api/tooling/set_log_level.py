import logging

def set_log_level(logger: Logger, level_str: str) -> None:
    level_str = level_str.upper()

    if level_str in logging._nameToLevel:
        logger.setLevel(logging._nameToLevel[level_str])
    else: # if the name got borked, default to debug
        logger.setLevel(logging._nameToLevel['DEBUG'])

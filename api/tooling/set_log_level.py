from logging import Logger, _nameToLevel

def set_log_level(logger: Logger, level_str: str) -> None:
    """
    Sets logging level for a provided Logger

    Args:
        logger (Logger): reference to an existing Logger
        level_str (str): case-insensitive text string for logging level, e.g. 'debug' for LOG_DEBUG.
    """
    level_str = level_str.upper()

    if level_str in _nameToLevel:
        logger.setLevel(_nameToLevel[level_str])
    else: # if the name got borked, default to debug
        logger.setLevel(_nameToLevel['DEBUG'])

    logger.info(f'logging level: {level_str}')
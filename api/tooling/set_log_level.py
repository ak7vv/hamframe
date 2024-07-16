from logging import Logger, _nameToLevel, getLevelName, getLevelNamesMapping

def set_log_level(logger: Logger, level_str: str) -> None:
    """
    Sets logging level for a provided Logger. If string doesn't match one of the defined values in the function (excludes NOTSET), set to DEBUG.

    Args:
        logger (Logger): reference to an existing Logger
        level_str (str): case-insensitive text string for logging level, e.g. 'debug' for LOG_DEBUG.
    """
    level_str = level_str.upper()

    log_levels = [
        'CRITICAL',
        'ERROR',
        'WARNING',
        'INFO',
        'DEBUG'
    ]

    logger.debug(f'level_str = {level_str}')

    if not level_str in log_levels:
        level_str = 'DEBUG'

    logger.setLevel(getLevelName(level_str))

    logger.info(f'logging level: {level_str} ({getLevelName(level_str)})')

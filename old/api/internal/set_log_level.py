import logging
import os
from time import sleep

def set_log_level(level_str: str) -> None:
    """
    Sets logging level for a provided Logger. If string doesn't match one of 
    the defined values in the function (excludes NOTSET), set to DEBUG.

    Args:
        logger (Logger): reference to an existing Logger
        level_str (str): case-insensitive text string for logging level, 
        e.g. 'debug' for LOG_DEBUG.
    """

    # access the 'global' logger
    logger = logging.getLogger('api')

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
        logger.critical('unrecognized LOG_LEVEL, exiting.')
        logger.debug('(sleeping for 5 seconds to reduce thrashing.)')
        sleep(5)
        os.sys.exit()

    logger.setLevel(logging.getLevelName(level_str))

    logger.info(f'logging level: {level_str} ({logging.getLevelName(level_str)})')

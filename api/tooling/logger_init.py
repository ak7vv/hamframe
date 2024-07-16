# Initialize logging

import logging
import sys

class CustomFormatter(logging.Formatter):
    """
    logging.Formatter to modify the logging format based on logging level
    """
    def __init__(self, fmt=None, datefmt=None, style='%', level_formats=None):
        super().__init__(fmt, datefmt, style)
        self.level_formats = level_formats or {}

    def format(self, record):
        if record.levelno in self.level_formats:
            self._style._fmt = self.level_formats[record.levelno]
        return super().format(record)

class ANSIColors:
    """ANSI escape sequences for colors to use in console text strings
    """
    green = '\033[32m'
    blue = '\033[34m'
    white = '\033[37m'
    yellow = '\033[33m'
    red = '\033[31m'
    bold_red = '\033[31;1m'
    cyan = '\036m'
    reset = '\033[0m'

# Define custom formats for each severity level
level_formats = {
    logging.DEBUG: ANSIColors.green + '%(levelname)s:' + ANSIColors.white + '\t  %(asctime)s %(module)s' + ANSIColors.green + ' %(message)s' + ANSIColors.reset,
    logging.INFO: ANSIColors.cyan + '%(levelname)s:' + ANSIColors.reset + '\t  %(message)s',
    logging.WARNING: ANSIColors.yellow + '%(levelname)s:' + ANSIColors.reset + '\t  %(message)s',
    logging.ERROR: ANSIColors.red + '%(levelname)s:' + ANSIColors.reset + '\t  %(message)s',
    logging.CRITICAL: ANSIColors.bold_red + '%(levelname)s:' + ANSIColors.reset + '\t  %(message)s'
}

def define_logger(startup_logging_level: str = 'INFO') -> logging.Logger:
    """
    Initialize logging.Logger with custom logging format based on logging severity level.

    Args:
        startup_logging_level (str, optional): Optional early logging level (i.e. 'DEBUG'). Defaults to 'INFO'.

    Returns:
        logging.Logger: returns a Logger with custom formatter/handler and level set (see Args).
    """

    formatter = CustomFormatter(level_formats=level_formats)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.addHandler(handler)

    # set_log_level(logger, 'debug') # normally not needed, enable for debugging of env variables only

    logger.setLevel(logging.getLevelName(startup_logging_level))

    return logger

logger = define_logger() # specify 'DEBUG' if early debugging (env) is needed

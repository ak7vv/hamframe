# Initialize logging

import logging
import sys

class CustomFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%', level_formats=None):
        super().__init__(fmt, datefmt, style)
        self.level_formats = level_formats or {}

    def format(self, record):
        if record.levelno in self.level_formats:
            self._style._fmt = self.level_formats[record.levelno]
        return super().format(record)

# https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
green = '\x1b[32;47m'
blue = '\x1b[34;47m'
grey = '\x1b[38;20m'
yellow = '\x1b[33;20m'
red = '\x1b[31;20m'
bold_red = '\x1b[31;1m'
reset = '\x1b[0m'

# Define custom formats for each severity level
level_formats = {
    logging.DEBUG: green + '%(levelname)s:' + grey + '\t  %(asctime)s %(module)s' + reset + ' %(message)s',
    logging.INFO: blue + '%(levelname)s:' + reset + '\t  %(message)s',
    logging.WARNING: yellow + '%(levelname)s:' + reset + '\t  %(message)s',
    logging.ERROR: red + '%(levelname)s:' + reset + '\t  %(message)s',
    logging.CRITICAL: bold_red + '%(levelname)s:' + reset + '\t  %(message)s'
}

def logger_init(startup_logging_level: str = 'INFO') -> logging.Logger:
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
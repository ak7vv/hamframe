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

# Define custom formats for each severity level
level_formats = {
    logging.DEBUG: '%(levelname)s:\t  %(asctime)s %(module)s %(message)s',
    logging.INFO: '%(levelname)s:\t  %(message)s',
    logging.WARNING: '%(levelname)s:\t  %(message)s',
    logging.ERROR: '%(levelname)s:\t  %(message)s',
    logging.CRITICAL: '%(levelname)s:\t  %(message)s'
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
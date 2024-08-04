import logging
from functools import wraps

from src.config.logger_config import logger


def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Function '{func.__name__}' called with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

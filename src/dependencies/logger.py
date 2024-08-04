from functools import wraps
from contextlib import redirect_stdout
import io
from config.logger_config import logger


def log_function(func):
    """
    Decorator that logs the call and return value of the decorated function.
    Also logs any exceptions raised by the function and captures print statements.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The wrapped function with logging.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        stream = io.StringIO()
        try:
            logger.info(f"Function '{func.__name__}' called with args: {args} and kwargs: {kwargs}")
            with redirect_stdout(stream):
                result = func(*args, **kwargs)

            output = stream.getvalue()
            if output:
                logger.info(f"Print output from '{func.__name__}':\n{output}")
            if result is None:
                logger.info(f"Function '{func.__name__}' completed without returning a value")
            else:
                logger.info(f"Function '{func.__name__}' returned {result}")
            return result
        except Exception as e:

            output = stream.getvalue()
            if output:
                logger.info(f"Print output from '{func.__name__}':\n{output}")
            logger.exception(f"Function '{func.__name__}' raised an exception: {e}")
            raise

    return wrapper

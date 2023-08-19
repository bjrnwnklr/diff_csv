from functools import wraps
import timeit


def runtimer(func):
    """Times a function and prints out the runtime."""

    @wraps(func)
    def _wrapper(*args, **kwargs):
        # do some timing
        start_time = timeit.default_timer()
        value = func(*args, **kwargs)
        # do some more timing and print
        duration = timeit.default_timer() - start_time
        print(f"Elapsed time to run {func.__name__}: {duration:.5f} seconds.")
        return value

    return _wrapper

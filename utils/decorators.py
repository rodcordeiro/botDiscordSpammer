import time
import sys

class gracefully_shutdown(object):

    def __init__(self, arg1):
        self.log = arg1

    def __call__(self, function, *args, **kwargs):
        def inner_func(*args, **kwargs):
            try:
                start_time = time.time()
                result = function(*args, **kwargs)
                end_time = time.time()
                self.log.debug(f"Method Name: {function.__name__}, Args: {args}, Kwargs: {kwargs}, Execution Time: {end_time - start_time}")
                return result
            except KeyboardInterrupt:
                self.log.info('exiting after keyboard.')
                sys.exit()
        return inner_func


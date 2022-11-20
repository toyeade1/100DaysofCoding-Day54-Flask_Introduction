import time


def speed_calc_decorator(function):
    def wrapper_function():
        time_started = time.time()
        function()
        time_ended = time.time()
        time_elapsed = round(time_ended - time_started, 2)
        print(f'The time elapsed for {function.__name__} is {time_elapsed} seconds ')

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
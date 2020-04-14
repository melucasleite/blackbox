import time


def exceeded_time(start_time, runtime):
    return (get_current_time() - start_time) > runtime


def temperature_reached(reading, temp):
    return reading == temp


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func

    return decorate


@static_vars(time=0)
def get_current_time():
    get_current_time.time += 1
    return get_current_time.time


#
# def get_current_time():
#     return time.time()


def log(message, type):
    if (type == "info"):
        print("[{}] {}".format(get_current_time() / (60 * 60 * 24), message))

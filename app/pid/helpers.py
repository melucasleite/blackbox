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
        time = display_time(get_current_time(), 4)
        print("[{}] {}".format(time, message))


def display_time(seconds, granularity=2):
    result = []
    intervals = (
        ('days', 60 * 60 * 24),  # 60 * 60 * 24
        ('hours', 60 * 60),  # 60 * 60
        ('minutes', 60),
        ('seconds', 1),
    )
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])

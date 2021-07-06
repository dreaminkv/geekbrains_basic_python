def type_logger(func):
    def wrapper(*args):
        result = func(*args)
        for i in args:
            yield f"{func.__name__}({i}: {type(result)} - {func(i)})),"
    return wrapper


@type_logger
def calc_cube(*args):
    for i in args:
        return i ** 3


test = calc_cube(5, 10, 13, 2)
print(*test)
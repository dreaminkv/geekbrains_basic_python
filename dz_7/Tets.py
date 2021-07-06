# def p_wrapper(func):
#     def tag_wrapper(*args, **kwargs):
#         tag_p = func(*args, **kwargs)
#         return f'<p>{tag_p}</p>'
#     return tag_wrapper
#
#
# @p_wrapper
# def render_input(field):
#     return f'<input id="id_{field}" type="text" name="{field}">'
#
#
# username_f = render_input('username')
# print(username_f)
def simple_cache(func):
    cache = {}
    def wrapper(*args):
        nonlocal cache
        key = str(*args)
        if key not in cache:
            cache[key] = func(*args)
            return cache[key]
    return wrapper


@simple_cache
def render_input(field):
    print(f"call render_input('{field}')")
    return f'<input id="id_{field}" type="text" name="{field}">'


username_f = render_input('username')
password_f = render_input('password')
username_f_2 = render_input('username')
username_f_3 = render_input('sf')
print(username_f)
print(password_f)
print(username_f_2)
print(username_f_3)
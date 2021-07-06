import re

RE_DATE = re.compile(r'(\w+)')
txt = 'someon_e@geekbrains.ru'
result = RE_DATE.findall(txt)
if len(result) < 3:
    raise ValueError(f'ValueError: wrong email: {txt}')
else:
    parse_dict = {'username': result[0], 'domain': result[1]}
    print(parse_dict)
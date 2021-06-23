# Написать функцию currency_rates(), принимающую в качестве
# аргумента код валюты (например, USD, EUR, GBP, ...) и возвращающую курс
# этой валюты по отношению к рублю. Использовать библиотеку requests. В
# качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть
# содержимое ответа. Можно ли, используя только методы класса str, решить поставленную
# задачу? Функция должна возвращать результат числового типа, например float. Подумайте:
# есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно
# ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого
# нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
# в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
import requests
import json
from sys import argv
LINK = 'https://www.cbr-xml-daily.ru/daily_json.js'


def what_course(*args):
    res = requests.get(LINK)
    for i in args:
        json_file = json.loads(res.text)['Valute'][i]['Value']
        json_valute = json.loads(res.text)['Valute'][i]['Name']
        yield f'курс {json_valute}: {json_file}'


if __name__ == '__main__':
    print(*what_course('USD', 'EUR', 'AUD'))


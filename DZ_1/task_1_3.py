#3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5
# — получаем «5 процентов», задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
#
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание. Пробуйте их
# решать, если уверены в своих силах.


def percent(num):
    percent = {1: '1 процент', 2: '2 процента', 3: '3 процента', 4: '4 процента',
               5: '5 процентов', 6: '6 процентов',
               7: '7 процентов', 8: '8 процентов', 9: '9 процентов', 10: '10 процентов',
               11: '11 процентов', 12: '12 процентов',
               13: '13 процентов', 14: '14 процентов', 15: '15 процентов', 16: '1 процентов',
               17: '17 процентов', 18: '18 процентов',
               19: '19 процентов', 20: '20 процентов'}
    return percent[num]


print(percent(7))
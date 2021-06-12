# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело
# на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание:
# использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из
# этого списка, сумма цифр которых делится нацело на 7. Внимание:
# новый список не создавать!!!
from copy import copy
odd_list = [i ** 3 for i in range(1000) if not i % 2 == 0]
print(odd_list)

a = [['hello'], 10]
b = copy(a)
print(id(a), id(b))  # 33907336 63072968
b[1] = 15
print(a, b)  # [['hello'], 10] [['hello'], 15]


def seven_remainder(odd):
    sum_nums = 0
    for i in odd:
        nums = 0
        elem = copy(i)
        while elem > 0:
            num = elem % 10
            elem = elem // 10
            nums = num + nums
        if nums % 7 == 0:
            sum_nums += i
    return sum_nums


print(seven_remainder(odd_list))
for id, item in enumerate(odd_list):
    odd_list[id] = item + 17
print(odd_list)
print(seven_remainder(odd_list))
# 17485588610
# 15392908808
# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело
# на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание:
# использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из
# этого списка, сумма цифр которых делится нацело на 7. Внимание:
# новый список не создавать!!!
odd_list = [i ** 3 for i in range(1000) if not i % 2 == 0]
print(odd_list)


def seven_remainder(odd):
    nu = 0
    for i in odd:
        nums = 0
        b = i
        while b > 0:
            num = b % 10
            b = b // 10
            nums = num + nums
        if nums % 7 == 0:
            nu += i
    return nu


print(seven_remainder(odd_list))
for id, item in enumerate(odd_list):
    odd_list[id] = item + 17
print(odd_list)
print(seven_remainder(odd_list))

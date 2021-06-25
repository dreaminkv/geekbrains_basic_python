# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать
# из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

not_unique_num = set()
tmp = set()

for i in src:
    if i not in tmp:
        tmp.add(i)
    elif i in tmp:
        not_unique_num.add(i)
unique_num = [i for i in src if i not in not_unique_num]

print(unique_num)

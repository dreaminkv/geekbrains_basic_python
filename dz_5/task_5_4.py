# 4 Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
dsrc = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
import sys
import random
from time import perf_counter

src = [i for i in random.sample(range(5 ** 10), 5 ** 10)]


def prev_max_num(list_src):
    gen_num_1 = (el for el in list_src)
    gen_num_2 = (el for el in list_src)
    next(gen_num_2)
    return (two for one, two in zip(gen_num_1, gen_num_2) if two > one)

    # start = perf_counter()
    # result = []
    # for i in range(len(list_src) - 1):
    #     if list_src[i + 1] > list_src[i]:
    #         result.append((list_src[i + 1]))
    # return sys.getsizeof(result), perf_counter() - start
    # result_gen = ((list_src[i + 1]) for i in range(len(list_src) - 1) if list_src[i + 1] > list_src[i])
    # print(perf_counter() - start)
    # return sys.getsizeof(result_gen), perf_counter() - start
#
#
print(*prev_max_num(src))
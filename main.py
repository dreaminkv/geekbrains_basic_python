a = [['hello'], 10]
b = a.copy()
print(id(a), id(b))  # 30433928 65563016
b[1] = 15
print(id(a[0]), id(b[0]))  # [['hello'], 10] [['hello'], 15]
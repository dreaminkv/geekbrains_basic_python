class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f'Matrix: {self.matrix}'

    def __add__(self, other):
        for i in range(len(self.matrix)):
            yield [x + y for x, y in zip(self.matrix[i],
                                          other.matrix[i])]


a = Matrix([[2, 5, 6], [5, 7, 8]])
b = Matrix([[6, 4, 5], [6, 8, 2]])
x = a + b
print(*x)
print(a)
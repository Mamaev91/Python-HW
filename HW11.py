# Создайте класс Матрица. Добавьте методы для:
# вывода на печать, сравнения, сложения,
# *умножения матриц


from functools import total_ordering
from random import randint

_MIN = 0
_MAX = 100
_SIZE = 3


class Matrix:
    """Создает объект Матрица из заданного списка"""
    _shift = 5

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self._size = len(self.matrix)

    def __eq__(self, other):
        for i in range(self._size):
            for j in range(self._size):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __add__(self, other):
        matrix_new = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self._size)] for i in range(self._size)]
        return Matrix(matrix_new)

    def __mul__(self, other):
        result = []
        for i in range(self._size):
            spam = []
            for j in range(self._size):
                eggs = []
                for k in range(self._size):
                    eggs.append(self.matrix[i][k] * other.matrix[k][j])
                spam.append(sum(eggs))
            result.append(spam)
        return Matrix(result)

    def __str__(self):
        result = [' '.join(f'{num:>{self._shift}}' for num in line) for line in self.matrix]
        return '\n'.join(result)

    def __repr__(self):
        return f'Matrix({self.matrix})'


if __name__ == '__main__':
    data1 = [[randint(_MIN, _MAX) for _ in range(_SIZE)] for _ in range(_SIZE)]
    m1 = Matrix(data1)
    print(f'{m1 = }', m1, sep='\n')
    data2 = [[randint(_MIN, _MAX) for _ in range(_SIZE)] for _ in range(_SIZE)]
    m2 = Matrix(data2)
    print(f'{m2 = }', m2, sep='\n')
    m3 = m1 + m2
    print(f'{m3 = }', m3, sep='\n')
    m4 = m1 * m2
    print(f'{m4 = }', m4, sep='\n')
    print(m1 == m2)
    print(m1 != m2)

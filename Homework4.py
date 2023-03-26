# 1. Напишите функцию для транспонирования матрицы

def transpose_matrix(a: list) -> list:
    res = []
    n = len(a)
    m = len(a[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [a[i][j]]
        res = res + [tmp]
    return res

matrix = [[3, 1, 7], [7, 5, 9]]

transpose_matrix(matrix)
print(matrix)


# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def number_dir(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[value] = key
    return result

print(number_dir(a=2, b=3, c=5))




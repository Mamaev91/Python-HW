class MyExceptions(Exception):
    pass


class MyMinLengthError(MyExceptions):

    def __init__(self, param, value):
        self.param = param
        self.value = value

    def __str__(self):

        if self.param < self.value:
            return f'Сторона треугольника не может быть меньше нуля\n' \
                   f'Заданное число {self.param} < {self.value}'
        elif self.param == self.value:
            return f'Сторона треугольника не может быть равна нулю\n' \
                   f'Заданное число {self.param} = {self.value}'


class MyTriangleError(MyExceptions):

    def __init__(self, value1: int, value2: int, value3: int):
        self.a = value1
        self.b = value2
        self.c = value3

    def __str__(self):
        print(f"Tреугольника со сторонами {self.a}, {self.b}, {self.c} не существует!")


class CheckBagSize(MyExceptions):

    def __init__(self, bag: int, items: int):
        self.bag = bag
        self.item = items

    def __str__(self):
        print(f"Предмет размером {self.item} не влезет в сумку размером {self.bag}!")



# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки(от 2 до 5) и результаты тестов(от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и
# по оценкам всех предметов вместе взятых.


import csv
import os
from pathlib import Path
from random import randint
from typing import Any


class STUDENTDescriptor:
    def __init__(self, name):
        self.name = name

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, name):
        self.validate(name)
        setattr(instance, self.param_name, name)

    def validate(self, name):
        if not name.isalpha():
            raise TypeError(f'Фамилия, имя и отчество могут состоять только из букв')
        if self.name is not None and not name.istitle():
            raise ValueError(f'Фамилия, имя и отчество начинаются с заглавной буквы')


def __csv_creator():
    dir_name = os.path.basename(os.getcwd())
    file = Path(f"{dir_name}.csv")
    fieldnames = ['subject', 'grade', 'test_result']
    subjects = ['math', 'literature', 'physics', 'informatics', 'english']
    grades = [(randint(2, 5) for _ in range(randint(2, 10))) for _ in range(5)]
    test_results = [(randint(0, 100) for _ in range(randint(2, 10))) for _ in range(5)]
    rows = []

    for subject, grade, test in zip(subjects, grades, test_results):
        rows.append([subject, [*grade], [*test]])

    with open(file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for subj_row in rows:
            writer.writerow(subj_row)

    return f


def csv_reader(file: Path) -> list[list[Any]]:
    subjects = []
    test_results = {}
    grades = {}
    __csv_creator()
    with open(file.name, 'r', encoding='utf-8') as f:
        data = list(csv.reader(f))[1:]
    for row in data:
        subjects.append(row[0])
        for i in row[1]:
            if i.isdigit():
                grades.setdefault(row[0], []).append(int(i))
        for j in row[2]:
            if j.isdigit():
                test_results.setdefault(row[0], []).append(int(j))
    return [subjects, grades, test_results]


class Student:
    name = STUDENTDescriptor('')
    surname = STUDENTDescriptor('')
    patronymic = STUDENTDescriptor('')

    def __init__(self, surname, name, patronymic):
        self.__test_results = None
        self.__grades = None
        self.dir_name = os.path.basename(os.getcwd())
        self.file = Path(f"{self.dir_name}.csv")
        self.__file = csv_reader(self.file)
        self.__subjects = csv_reader(self.file)[0]
        self._name = name
        self._surname = surname
        self._patronymic = patronymic

    def test_calcs(self):
        self.__test_results = self.__file[2]
        avg_tests = {}

        for subject, grades in self.__test_results.items():
            avg_tests.setdefault(subject, 0)
            avg_tests[subject] = f"{(sum(grades) / len(grades)):.2f}"
        return avg_tests

    def grades_calcs(self):
        self.__grades = self.__file[1]
        nums = []
        for grades in self.__grades.values():
            for i in grades:
                nums.append(i)
        avg_total = f"{(sum(nums) / len(nums)):.2f}"
        return avg_total

    def __str__(self):
        return f"Student: {self._surname} {self._name} {self._patronymic}\nSubjects: {self.__subjects}\n" \
               f"Average test results: {self.test_calcs()}\nAverage grade total: {self.grades_calcs()}"


if __name__ == '__main__':
    stud = Student('Baranchik', 'Denis', 'Sergeevich')
    print(stud)
    print(f"{stud.test_calcs() = }")
    print(f"{stud.grades_calcs() = }")
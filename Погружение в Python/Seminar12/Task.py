#  Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# - Экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
from collections import OrderedDict


class CapitalizedString:
    """Проверяет что все элементы строки имеют только буквы и начинаются с большой"""
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __set__(self, instance, value: [str]):
        for elem in value:
            if not (elem.istitle() and elem.isalpha()):
                raise ValueError("Имя должно быть с большой буквы и иметь только буквы")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return " ".join(map(str, instance.__dict__[self.name]))


class Range:
    """Создаёт ограниченый список разрешённых чисел"""
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value} ')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')


class FixedDict(dict):
    """Устанавливает запрет на изминение списка уроков"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key in self:
            super().__setitem__(key, value)
        else:
            raise KeyError(f"Запрет на изминение списка уроков")


class Student:
    full_name = CapitalizedString()
    school_class = Range(1, 11 + 1)
    # Я решил добавить в оценки 0 и 1 так как колы тоже ставят, а ещё ученик может пропустить контрольную
    assessments = Range(0, 5 + 1)
    assessments_test = Range(0, 100 + 1)
    schedule = {}

    def __init__(self, name: str, school_class: int):
        self.full_name = name.split(" ")
        self.school_class = school_class
        self.schedule = FixedDict(self.collection_of_information(self.school_class))

    def __str__(self):
        def calculate_gpa(quantity, quality):
            return round(quality / quantity, 2) if quantity > 0 else 0.0

        result = f"Студент {self.full_name} имеет слудующий оценки:\n"

        all_lessons = {"quantity": 0, "quality": 0}
        all_tests = {"quantity": 0, "quality": 0}

        for key, value in self.schedule.items():
            elems = [elem for elem in value if elem and elem > 0]
            gpa = calculate_gpa(len(elems), sum(elems))
            result += f'{key} - {gpa} - {[elem for elem in value]}\n'

            target_dict = all_tests if "test" in key else all_lessons
            target_dict["quality"] += sum(elems)
            target_dict["quantity"] += len(elems)

        all_gpa = calculate_gpa(all_lessons["quantity"], all_lessons["quality"])
        all_gpa_t = calculate_gpa(all_tests["quantity"], all_tests["quality"])
        result += f"Средний балл по всем тестам - {all_gpa_t}\n"
        result += f"Средний балл по всем предметам - {all_gpa}"
        return result

    @staticmethod
    def collection_of_information(school_class: int) -> OrderedDict:
        # Чтение CSV-файла
        file_path = 'lessons' + str(school_class) + '.csv'
        data = OrderedDict()

        with open(file_path, mode='r', newline='') as file:
            row = next(csv.reader(file))
            for elem in row:
                data[elem] = []
                data[elem + '_test'] = []

        return data

    def add_assessment(self, key, value):
        if 'test' in key:
            self.assessments_test = value
            self.schedule[key].append(self.assessments_test)
        else:
            self.assessments = value
            self.schedule[key].append(self.assessments)


if __name__ == "__main__":
    a = Student("Asdf Fsdf", 11)
    # b = Student("Asdf 0sdf", 11)
    print(a.full_name)
    # a.schedule["asd"] = []
    a.add_assessment("a", 3)
    a.add_assessment("b", 5)
    a.add_assessment("b", 5)
    # a.add_assessment("a", 7)
    a.add_assessment("a_test", 49)
    a.add_assessment("a_test", 3)
    a.add_assessment("a_test", 89)
    a.add_assessment("a_test", 12)
    # a.add_assessment("a_test", 150)
    print(a.schedule)
    print(a)

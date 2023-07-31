# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def data_processing(data: str) -> tuple | None:
    try:
        index = data.rfind('/') + 1
        if index == 0:
            raise ValueError()
        path, file = data[:index], data[index:]
        file, form = file.split('.')
        return path, file, form
    except ValueError:
        return None


if __name__ == "__main__":
    PATH_TO_FILE = 'ASDFASDF/ASD/A/SD/FA/SDF/ASD/Free.py'
    print(data_processing(PATH_TO_FILE))

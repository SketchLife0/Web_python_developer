# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.

from pathlib import Path
# import platform


def rename(extension_old: str, extension_new="", wanted_name="", count_nums=0, band=None, path=""):
    """
    Переименует все файлы в папке в которой вызывается
    :param extension_old: Старый формат
    :param extension_new: Новый формат
    :param wanted_name: Желаемое имя
    :param count_nums: Количество символов на нумерацию
    :param band: Лист двух положительных индексов
    :param path: Путь к файлам
    :return:
    """
    err = None if (isinstance(band, list) and len(band) == 2) or band is None else ValueError("Некорректные индексы")
    if err:
        raise err

    # Сначала я написал это, а потом вспомнил про elem.parent и elem.name. Было жалко удалять
    # separator = ''
    # match platform.system():
    #     case "Windows":
    #         separator = "\\"
    #     case "Linux", "Darwin":
    #         separator = "/"
    # if not separator:
    #     raise AttributeError("Неизвестная операционная система")

    if not extension_new:
        extension_new = extension_old
    if path:
        folder = Path(path)
    else:
        folder = Path.cwd()

    numerator = 1
    num = str(numerator)
    if len(num) <= count_nums:
        for _ in range(count_nums - len(num)):
            num = "0" + num
    else:
        num = ""

    for elem in folder.iterdir():
        print(elem)
        path_to_file = elem.parent
        file_name = elem.name
        i = file_name.rfind(extension_old)
        if i == -1:
            continue
        file_name = file_name[:i]
        old_name = ""
        if band and not (band[0] < 0 or band[1] > len(file_name) - 1):
            old_name = file_name[band[0]:band[1]+1]
        file_name = old_name + (wanted_name if wanted_name else file_name[:i]) + num + extension_new
        numerator += 1
        elem.rename(path_to_file / file_name)

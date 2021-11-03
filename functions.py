# Импорт библиотек
import os
import time
import pandas as pd


# ---------------------------------------------------------------------------------------------------------------------
"""
Импорт данных из кофигурационного файла
"""
try:
    from config import PATH
except ImportError:
    raise Exception('Файл или модули не найдены')


# ---------------------------------------------------------------------------------------------------------------------
def print_mes(mes_, end_=False):
    """
    Оформление сообщения в логи
    :param end_:
    :param mes_: (str) Сообщение
    :return: Выводит отформатированное сообщение
    """
    ending = '\n' if end_ else ''
    print(f'----{mes_}----{ending}')


def print_warn(mes_):
    """
    Оформление предупреждения в логи
    :param mes_: (str) Сообщение
    :return: Выводит отформатированное сообщение
    """
    print(f'!!!!{mes_}!!!!')


# ---------------------------------------------------------------------------------------------------------------------
def check_format(file_):
    """
    Проверка формата файла
    :param file_: (str) Название файла, включая его расширение
    :return: (bool) Возвращает True, если файл соответсвует форматам
    """
    return True if file_.endswith(('.csv', '.txt')) else False


def check_format_delimiter(name_):
    """
    Проверка формата файла для определения правльного разделителя
    :param name_: (str) Название файла, включая его расширение
    :return: (str) Разделитель '\t' (знак табуляции) для файла с форматом .txt или ';' для .csv
    """
    delimiter = ';'
    if name_[-3:] == 'txt':
        delimiter = '\t'
    return delimiter


def comp_path(path_, name_):
    """
    Объединение в одну строку название файла и пути до него
    :param path_: (str) Путь до файла
    :param name_: (str) Название файла
    :return: С
    """
    return f'{path_}/{name_}'


def get_name_var(variable_):
    """
    Получение названия переменной в коде
    :param variable_: (Any) Любая переменная, объявленная в коде
    :return: (str) Название переменной
    """
    return f'{variable_=}'.split('=')[0]


# ---------------------------------------------------------------------------------------------------------------------
def read_file(path_):
    """
    Чтение данных файла и запись их в таблицу
    :param path_: (str) Путь до файла + имя
    :return: (pandas DataFrame) Таблица с данными
    """
    return pd.read_csv(path_, names=['numbers'],
                       delimiter=check_format_delimiter(path_), dtype=object, index_col=False)


def delete_duplicates(df_):
    """
    Удаление дубликатов внутри таблицы
    :param df_: (pandas DataFrame) Таблица с данными
    :return: (pandas DataFrame) Таблица с данными, очищенными от дубликатов
    """
    df_.drop_duplicates(subset='numbers', inplace=True)
    df_.reset_index(drop=True, inplace=True)
    return df_


def get_all_in_folder(dct_, path_):
    """
    Получение и сохранение всех файлов в папке в таблицы
    :param dct_: (dict) Словарь для сохранения данных
    :param path_: (str) Путь до файла
    :return: (dict) Словарь с полученными таблицами
    """
    count = 0

    for filename in os.listdir(path_):
        if check_format(filename):
            dct_[str(count)] = {
                'df': delete_duplicates(read_file(comp_path(path_, filename))),
                'name': filename,
                'len': 0
            }
            dct_[str(count)]['len'] = dct_[str(count)]['df'].shape[0]

            count += 1

    return dct_


def create_dir(path_):
    os.mkdir(path_)


# ---------------------------------------------------------------------------------------------------------------------
def check_limit(path, limit):
    base_size = os.path.getsize(path)
    if base_size > limit:
        name, format_file = path[:-4], path[-4:]
        rows_in_one_file = round(
            sum(1 for _ in open(path)) / ((base_size // limit) + 1)
        )

        header = None
        small_file = None
        start = 0
        with open(path, "r", encoding="utf8") as in_file:
            lines = in_file.readlines()
            if 'phone' in lines[0].lower():
                header = lines[0]
                start = 1
            count = 0
            for i, line in enumerate(lines[start:]):
                if i % rows_in_one_file == 0:
                    if small_file:
                        small_file.close()
                    count += 1
                    small_filename = f'{name}_{count}.{format_file}'
                    small_file = open(small_filename, "w")
                    if header:
                        small_file.write(header)
                small_file.write(line)
            if small_file:
                small_file.close()
        os.remove(path)


def print_logs(function):
    """
    Декоратор для функций - выводит время выполнения
    """
    def accept_arg(*args):
        start_time = time.time()
        function(*args)
        print_mes(f'Время выполнения: {time.time() - start_time:.4f} секунд', True)
    return accept_arg

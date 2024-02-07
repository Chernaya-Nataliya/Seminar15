'''Задание №6
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.
'''
import logging
import os
from collections import namedtuple

logging.basicConfig(filename='Seminar15/Log/ex_6.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname} - {asctime} : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

Data = namedtuple('Data', ['file_name', 'file_exten', 'dir_flag', 'parent_dir'])

def collect_directory_info(directory_path):
    clas_list = []

    for root, dirs, files in os.walk(directory_path):
        parent_dir = os.path.basename(root)
        
        for folder in dirs:
            dir_flag = 'Yes'
            file_name = folder
            file_exten = ''
            data = Data(file_name, file_exten, dir_flag, parent_dir)
            clas_list.append(data)
            logger.info(f'{file_name}, {file_exten}, {dir_flag}, {parent_dir}')

        for file in files:
            dir_flag = 'No'
            file_name, file_exten = os.path.splitext(file)
            data = Data(file_name, file_exten, dir_flag, parent_dir)
            clas_list.append(data)
            logger.info(f'{file_name}, {file_exten}, {dir_flag}, {parent_dir}')

    return clas_list

if __name__ == "__main__":
    directory_path = r'D:\GB\ГБ\Погружение в Python'
    directory_info = collect_directory_info(directory_path)
    print(*directory_info, sep="\n")

'''Задание №1
📌 Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
📌 Например отлавливаем ошибку деления на ноль.
'''

import os
import logging

log_directory = 'Log'
os.makedirs(log_directory, exist_ok=True)

logging.basicConfig(filename='Seminar15/Log/ex_1.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        logger.error(
            f'Ошибка деления на ноль! Число {a} нельзя поделить на число {b}')
        logger.info(
            f'Пример')

        return float('inf')
    return res


if __name__ == '__main__':
    print(f'{division(14, 2)}')
    print(f'{division(14, 0)}')
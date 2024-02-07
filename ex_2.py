'''Задание №2
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.

'''

import logging

logging.basicConfig(filename='Seminar15/Log/ex_2.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке '
                           '{lineno} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'аргументы функции: {args}, результат функции: {result}')
        return result

    return wrapper


@decor
def power(x, y):
    return x ** y


print(power(2, 10)) 
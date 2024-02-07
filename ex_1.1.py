import os
import logging
import argparse

def setup_logger():
    log_directory = os.path.join(os.path.dirname(__file__), 'Log')
    os.makedirs(log_directory, exist_ok=True)

    log_file = os.path.join(log_directory, 'ex_1.1.log')

    logging.basicConfig(filename=log_file,
                        filemode='w',
                        encoding='utf-8',
                        format='{levelname} - {asctime} в строке {lineno} '
                               'функция "{funcName}()" : {message}',
                        style='{',
                        level=logging.INFO)
    return logging.getLogger(__name__)

def division(a, b, logger):
    try:
        res = a / b
    except ZeroDivisionError as e:
        error_message = f'Ошибка деления на ноль! Число {a} нельзя поделить на число {b}'
        logger.error(error_message)
        print(error_message)
        logger.info(
            f'Пример')
        exit(1)  # Завершаем выполнение программы с ненулевым кодом выхода

    return res




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Программа для деления двух чисел")
    parser.add_argument("numerator", type=int, help="Числитель")
    parser.add_argument("denominator", type=int, help="Знаменатель")
    args = parser.parse_args()

    logger = setup_logger()  # Инициализируем логгер

    result = division(args.numerator, args.denominator, logger)
    print(f'Результат деления: {result}')



# запуск командной строкой:python ex_1.1.py 14 2
   # PS D:\GB\ГБ\Погружение в Python\Seminar\15\VS\Seminar15> python ex_1.1.py 14 2                                                             
   # Результат деления: 7.0

# запуск командной строкой:python ex_1.1.py 0 15
    # PS D:\GB\ГБ\Погружение в Python\Seminar\15\VS\Seminar15> python ex_1.1.py 0 15
    # Результат деления: 0.0
    
# # запуск командной строкой:python ex_1.1.py 14 0
    #PS D:\GB\ГБ\Погружение в Python\Seminar\15\VS\Seminar15> python ex_1.1.py 14 0                                                             
    #Ошибка деления на ноль! Число 14 нельзя поделить на число 0
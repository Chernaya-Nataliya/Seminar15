'''Задание №4
Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату'''

import logging
from datetime import datetime, timedelta

logging.basicConfig(filename='Seminar15/Log/ex_4.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.ERROR)


def find_date(description):
    months = {"января": 1, "февраля": 2, "марта": 3, "апреля": 4, "мая": 5, "июня": 6,
                "июля": 7, "августа": 8, "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12}
    days = {"понедельник": 0, "вторник": 1, "среда": 2, "четверг": 3, "пятница": 4, "суббота": 5, "воскресенье": 6}

    try:
        parts = description.split()
        if len(parts) != 3:
            raise ValueError("Некорректный формат строки")

        week_number = int(parts[0][:-2])
        day_of_week = days[parts[1]]
        month = months[parts[2]]

        current_year = datetime.now().year
        first_day_of_month = datetime(current_year, month, 1)
        first_requested_day = first_day_of_month + timedelta(days=(day_of_week - first_day_of_month.weekday() + 7) % 7)
        final_date = first_requested_day + timedelta(weeks=week_number - 1)

        return final_date.date()

    except Exception as e:
        logging.error(f"Ошибка при анализе строки: {e}")


print(find_date("1-й четверг ноября"))

'''
Планер.
Принимает из csv список задач с временем выполнения для каждой задачи.
Из первой строки файла берет время старта и время перерыва
Выдает распланированный расчет времени в txt файле

'''

import csv
from datetime import datetime, timedelta
import os
from time import sleep
from logger_func import log_func


def create_example_csv():
    a = [
        ['12:30', '10', '(start_time, time_out min)'],
        ['task 1', '1-31'],
        ['task 2', '1-00'],
        ['task 3', '1-00'],
        ['task 4', '0-40'],
        ['task 5', '0-20'],
        ['task 6', '0-40'],
        ['task 7', '2-13'],
    ]

    with open('tasks.csv', 'w', newline='') as file:
        csv.writer(file).writerows(a)


def count_tasktime(obj):
    '''
    извлекает из csv объекта все строки,
    возвращает словарь по типу {задание:(начало, конец),} и время перерыва в
    header_row[1]
    '''
    dict_tasks = {}
    header_row = next(obj)
    dt = datetime.strptime(header_row[0], "%H:%M")
    for t in obj:
        try:
            task = t[0]
            time = t[1]
        except IndexError:
            return
        task_hour, task_minute = time.split('-')
        new = dt + timedelta(hours=int(task_hour), minutes=int(task_minute))
        dict_tasks[task] = [dt, new]
        dt = new + timedelta(minutes=int(header_row[1]))
    return dict_tasks, header_row[1]


def read_csv_file():
    with open('tasks.csv', 'r') as file:
        read = csv.reader(file)
        try:
            dict_tasks, time_out = count_tasktime(read)
            return dict_tasks, time_out
        except ValueError as Err:
            logger.error(f'! read_csv_file - {name} - {Err}')
        except NameError as Err:
            logger.error(f'! read_csv_file - {name} - {Err}')
        return None, None


def write_txt_file(dict_task, time_out):
    with open('tasks.txt', 'w') as f:
        try:
            for a, b in dict_tasks.items():
                start = f'{b[0].hour}:{str(b[0].minute).zfill(2)}'
                finish = f'{b[1].hour}:{str(b[1].minute).zfill(2)}'
                f.write(f'{a}\nstart -  {start}, finish - {finish}\n\
                    Timeout: {time_out} minuts\n\n\n')
        except AttributeError as Err:
            logger.error(f'! write_txt_file - {name} - {Err}')
            f.write(f'Error - {Err}.\nWrong filling tasks.csv')
        except:
            logger.error(f'! write_txt_file - unrecognize error.\nWrong filling tasks.csv')
            f.write(f'! write_txt_file - unrecognize error ')




if __name__ == '__main__':

    name = 'planer.py'
    logger = log_func(name)

    try:
        dict_tasks, time_out = read_csv_file()
    except FileNotFoundError:
        create_example_csv()
        dict_tasks, time_out = read_csv_file()
    finally:
        write_txt_file(dict_tasks, time_out)




'''
на заметку PENDULUM

import pendulum

dt = pendulum.datetime(2012, 1, 31, 12, 12, 12)
print(dt.to_datetime_string())
dt_2 = dt.subtract(years=3, months=2, days=6, hours=12, minutes=31, seconds=43)
print(dt_2.to_datetime_string())
dt_3 = dt_2.add(years=3, months=2, days=6, hours=12, minutes=31, seconds=43)
print(dt_3.to_datetime_string())

2012-01-31 12:12:12
2008-11-23 23:40:29
2012-01-30 12:12:12
'''

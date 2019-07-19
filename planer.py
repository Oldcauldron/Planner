
'''
Планер.
Принимает из csv список задач с временем выполнения для каждой задачи.
Из первой строки файла берет время старта и время перерыва
Выдает распланированный расчет времени в txt файле

'''

import csv
from datetime import datetime, timedelta


def create_example_csv():
    a = [
        ['12:30', '10', '(start_time, time_out min)'],
        ['zadacha 1', '1-31'],
        ['zadacha 2', '1-00'],
        ['zadacha 3', '1-00'],
        ['zadacha 4', '0-40'],
        ['zadacha 5', '0-20'],
        ['zadacha 6', '0-40'],
        ['zadacha 7', '2-13'],
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
        dict_tasks, time_out = count_tasktime(read)
        return dict_tasks, time_out


def write_txt_file(dict_tasks, time_out):
    with open('tasks.txt', 'w') as f:
        for a, b in dict_tasks.items():
            start = f'{b[0].hour}:{str(b[0].minute).zfill(2)}'
            finish = f'{b[1].hour}:{str(b[1].minute).zfill(2)}'
            f.write(f'{a}\nstart -  {start}, finish - {finish}\n\
                Timeout: {time_out} minuts\n\n\n')


try:
    dict_tasks, time_out = read_csv_file()
except FileNotFoundError:
    create_example_csv()
    dict_tasks, time_out = read_csv_file()
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

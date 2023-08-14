import os
import random
# import calendar

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_Ru')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        email=faker_ru.email(),
        age=random.randint(20, 80),
        salary=random.randint(5000, 9000),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        phone_10=random.randint(10 ** 9, 10 ** 10 - 1),
        birthday=generate_random_date()
    )


def generate_random_date():
    # Генерация случайного месяца (от 1 до 12)
    month = random.randint(1, 12)
    # Генерация случайного дня в зависимости от месяца
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month == 2:
        day = random.randint(1, 28)  # Февраль
    else:
        day = random.randint(1, 30)
    # Генерация случайного года (от 1900 до 2099, например)
    year = random.randint(1950, 2000)
    # Получение названия месяца
    # month_name = calendar.month_name[month]
    # Формирование даты в нужном формате
    # date = f"{day:02d} {month_name},{year}"
    hour = random.randint(0, 24)
    minute = (random.sample([0, 15, 30, 45], k=1))
    return day, month, year, hour, *minute


def generated_file(desc='txt'):
    # получаем путь к директории текущего исполняемого файла и выходим в папку на один уровень выше
    current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, f'filetest_{random.randint(1, 999)}.{desc}')
    with open(file_path, "w+") as my_file:
        my_file.write(f"Hello world_{random.randint(0, 777)}")
    my_file.close()
    return my_file.name, file_path


def convert_to_12_hour_format(time_24h):
    # Преобразование времени из 24-часового формата в 12-часовой формат
    hour, minute = map(int, time_24h.split(":"))

    if hour == 0:
        return f"12:{minute:02d} AM"
    elif 1 <= hour <= 11:
        return f"{hour}:{minute:02d} AM"
    elif hour == 12:
        return f"12:{minute:02d} PM"
    else:
        return f"{hour - 12}:{minute:02d} PM"


def convert_to_24_hour_format(time_12h):
    # Преобразование времени из 12-часового формата в 24-часовой формат
    time_parts = time_12h.split()
    hour, minute = map(int, time_parts[0].split(":"))

    if time_parts[1].upper() == "AM":
        if hour == 12:
            hour = 0
    elif time_parts[1].upper() == "PM":
        if hour != 12:
            hour += 12
    return f"{hour:02d}:{minute:02d}"

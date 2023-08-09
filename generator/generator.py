import os
import random

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
    # Формирование даты в нужном формате
    date = f"{month:02d}/{day:02d}/{year}"
    return date


def generated_file(desc='txt'):
    # получаем путь к директории текущего исполняемого файла и выходим в папку на один уровень выше
    current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, f'filetest_{random.randint(1, 999)}.{desc}')
    with open(file_path, "w+") as my_file:
        my_file.write(f"Hello world_{random.randint(0, 777)}")
    my_file.close()
    return my_file.name, file_path

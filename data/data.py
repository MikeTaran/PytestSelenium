from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    phone_10: int = None
    birthday: tuple = None


@dataclass
class Date:
    day: int = None
    month: int = None
    year: int = None
    hour: int = None
    minute: int = None

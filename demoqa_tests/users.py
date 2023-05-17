import dataclasses
from datetime import date
from enum import Enum
from typing import List


class Gender(Enum):
    Female = 'female'
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Subject(Enum):
    english = 'English'
    maths = 'Maths'
    physics = 'Physics'
    chemistry = 'Chemistry'
    computer_science = 'Computer Science'
    economics = 'Economics'
    arts = 'Arts'
    biology = 'Biology'


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: List[Gender]
    mobile: str
    birth_day: str
    birth_month: str
    birth_year: str
    subjects: List[Subject]
    hobbies: List[Hobby]
    picture: str
    address: str
    state: str
    city: str





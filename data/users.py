import dataclasses


@dataclasses
class User:
    fisrt_name: str
    second_name: str
    email: str
    gender: str
    phone_number: str
    subjects: str
    picture: str
    address: str
    state: str
    city: str
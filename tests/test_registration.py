from datetime import date

from demoqa_tests.users import Hobby, Gender, User, Subject
from demoqa_tests.registration_page import RegistrationPage


def test_filling_form(browser_management):
    registration_page = RegistrationPage()
    student = User(
        first_name='Larisa',
        last_name='Badmaeva',
        email='larilotus12@gmail.com',
        gender=Gender.female,
        mobile='8902208866',
        birth_day='12',
        birth_month='July',
        birth_year='1991',
        subjects=[Subject.maths],
        hobbies=[Hobby.sports],
        picture='IMG_4499.jpg',
        address='Moscow',
        state='NCR',
        city='Delhi'
    )

    registration_page.open()

    # WHEN
    registration_page.fill_form(student)

    # THEN
    registration_page.assert_registration(student)

# TODO: finish implementation

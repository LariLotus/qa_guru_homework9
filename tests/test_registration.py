from datetime import date

from demoqa_tests.users import Hobby, Gender, User, Subject
from demoqa_tests.registration_page import RegistrationPage


def test_submit_form(browser_management):
    registration.page = RegistrationPage()
    student = User(
        first_name='Larisa',
        last_name='Badmaeva',
        email='larilotus12@gmail.com',
        gender=Gender.Female,
        mobile='8902208866',
        date_of_birth=date(1991, 7, 12),
        subject=Subject.math,
        hobby=Hobby.sports,
        picture='IMG_4499.jpg',
        address='Moscow',
        state='NCR',
        city='Delhi'
    )

    registration.page = RegistrationPage()
    registration.page.open()

    #WHEN
    registration.page.fill_form(student)

    #THEN
    registration.page.assert_registration(student)











    # TODO: finish implementation

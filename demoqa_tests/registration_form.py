from selene import browser, have
import os

from demoqa_tests import resource


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def choose_gender(self):
        browser.element('[value="Female"]').double_click()

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').element('[value="1991"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').element('[value="6"]').click()
        browser.element('.react-datepicker__day--012').click()

    def fill_subjects(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def choose_hobies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()

    def upload_picture(self, picture):
        browser.element('#uploadPicture').set_value(resource.path(picture))

    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)

    def choose_state_and_city(self, state, city):
        browser.element('#react-select-3-input').type(state).press_enter()
        browser.element('#react-select-4-input').type(city).press_enter()

    def submit(self):
        browser.element('#submit').press_enter()

    def assert_registration(self, student_name, student_email, student_gender, student_mobile, student_date_of_birth,
            student_subjects, student_hobbies, student_picture, student_current_address, student_state_and_city):
        browser.all('tbody tr').should(have.exact_texts(student_name, student_email, student_gender, student_mobile,
                                                        student_date_of_birth,student_subjects, student_hobbies,
                                                        student_picture, student_current_address, student_state_and_city
                                                        ))

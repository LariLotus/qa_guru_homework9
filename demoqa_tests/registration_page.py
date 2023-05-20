from selene import browser, have
import os


from demoqa_tests.users import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_form(self, student: User):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').type(student.last_name)
        browser.element('#userEmail').type(student.email)
        browser.element('[value="Female"]').double_click()
        browser.element('#userNumber').type(student.mobile)

        browser.element('#dateOfBirthInput').press()
        browser.element('.react-datepicker__year-select').send_keys(student.birth_year)
        browser.element('.react-datepicker__month-select').send_keys(student.birth_month)
        browser.element(f'.react-datepicker__day--0{student.birth_day}').click()

        for subject in student.subjects:
            browser.element('#subjectsInput').type(subject.value).press_enter()

        for hobby in student.hobbies:
            browser.all('.custom-checkbox').element_by(have.exact_text(hobby.value)).click()

        browser.element('#uploadPicture').send_keys(os.getcwd() + f"/resources{student.picture}")

        browser.element('#currentAddress').type(student.address)

        browser.element('#react-select-3-input').type(student.state).press_enter()
        browser.element('#react-select-4-input').type(student.city).press_enter()

        browser.element('#submit').press_enter()

    def assert_registration(self, student: User):
        full_name = f'{student.first_name} {student.last_name}'
        birthday = f'{student.birth_day} {student.birth_month},{student.birth_year}'
        state_and_city = f'{student.state} {student.city}'
        subjects = ','.join([subject.value for subject in student.subjects])
        hobbies = ','.join([hobby.value for hobby in student.hobbies])

        browser.all('tbody tr').should(have.exact_texts(
            f'Student Name {full_name}',
            f'Student Email {student.email}',
            f'Gender {student.gender.female.value}',
            f'Mobile {student.mobile}',
            f'Date of Birth {birthday}',
            f'Subjects {subjects}',
            f'Hobbies {hobbies}',
            f'Picture {student.picture}',
            f'Address {student.address}',
            f'State and City {state_and_city}')
            )




from demoqa_tests.registration_form import RegistrationPage


def test_submit_form(browser_management):
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Larisa')
    registration_page.fill_last_name('Badmaeva')
    registration_page.fill_email('larilotus12@gmail.com')
    registration_page.choose_gender()
    registration_page.fill_phone_number('8902208866')
    registration_page.fill_date_of_birth('1991', 'July', '12')
    registration_page.fill_subjects('Maths')
    registration_page.choose_hobies('Sports')
    registration_page.upload_picture('IMG_4499.jpg')
    registration_page.fill_current_address('Moscow')
    registration_page.choose_state_and_city('NCR', 'Delhi')
    registration_page.submit()

    registration_page.assert_registration(
        'Student Name Larisa Badmaeva',
        'Student Email larilotus12@gmail.com',
        'Gender Female',
        'Mobile 8902208866',
        'Date of Birth 12 July,1991',
        'Subjects Maths',
        'Hobbies Sports',
        'Picture IMG_4499.jpg',
        'Address Moscow',
        'State and City NCR Delhi'
    )









    # TODO: finish implementation

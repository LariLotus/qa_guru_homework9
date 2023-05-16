from demoqa_tests import RegistrationPage


def test_submit_form():
    registration_page = RegistrationPage
    registration_page.open()

    registration_page.fill_first_name('Larisa')
    registration_page.fill_last_name('Badmaeva')
    registration_page.fill_email('larilotus12@gmail.com')
    registration_page.choose_gender('Female')
    registration_page.fill_phone_number('8902208866')
    registration_page.fill_date_of_birth('12 July,1991')
    registration_page.fill_subjects('Math')
    registration_page.choose_hobies('Sports')
    registration_page.upload_picture('IMG_4499.jpg')
    registration_page.fill_current_address('Moscow')
    registration_page.choose_state_and_city('NCR Delhi')
    registration_page.submit()

    registration_page.assert_registration(
        'Larisa Badmaeva',
        'larilotus12@gmail.com',
        'Female',
        '8902208866',
        '12 July,1991',
        'Math',
        'Sports',
        'IMG_4499.jpg',
        'Moscow',
        'NCR Delhi'
    )









    # TODO: finish implementation

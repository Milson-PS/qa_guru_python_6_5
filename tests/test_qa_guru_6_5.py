import os
from selene import browser, have


def test_check_form():
    browser.open('https://demoqa.com/automation-practice-form')

    # Filling out the form
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('Ivanov@yandex.ru')
    browser.element('label[for="gender-radio-1').click()
    browser.element('#userNumber').type('89000000000')

    # Date of birth
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('option[value="5"]').click()  # Июнь
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('option[value="1994"]').click()
    browser.element('.react-datepicker__day--017').click()

    # Filling out the form
    browser.element('#subjectsInput').type('IT')

    # load file
    browser.element('#uploadPicture').send_keys(os.path.abspath('image/cat.jpg'))

    # Choosing a city
    browser.element('#currentAddress').type('123 Street, City, Country')
    browser.element('#state').click()
    browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    browser.all("#city div").element_by(have.exact_text("Delhi")).click()

    # Send form
    browser.element('#submit').click()

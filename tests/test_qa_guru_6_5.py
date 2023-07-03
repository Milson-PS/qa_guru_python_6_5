import os
from selene import browser, have


def test_check_form(browser_management):
    browser.open('/automation-practice-form')
    # Filling out the form
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('Ivanov@yandex.ru')
    browser.element('label[for="gender-radio-1').click()
    browser.element('#userNumber').type('8900000000')

    # Date of birth
    browser.element('#dateOfBirthInput').click()
    browser.element('[value="1991"]').click()
    browser.element('[value="5"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--004"]').click()

    # Filling out the form
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()

    # load file
    browser.element('#uploadPicture').send_keys(os.path.abspath('image/cat.jpg'))

    # Choosing a city
    browser.element('#currentAddress').type('123 Street, City, Country')
    browser.element('#state').click()
    browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    browser.all("#city div").element_by(have.exact_text("Delhi")).click()
    browser.element('#submit').click()

    # Expected Result
    browser.element('.modal-header').should(have.exact_text('Thanks for submitting the form'))
    browser.all('.modal-body tr td')[1].should(have.exact_text('Ivan Ivanov'))
    browser.all('.modal-body tr td')[3].should(have.exact_text('Ivanov@yandex.ru'))
    browser.all('.modal-body tr td')[5].should(have.exact_text('Male'))
    browser.all('.modal-body tr td')[7].should(have.exact_text('8900000000'))
    browser.all('.modal-body tr td')[9].should(have.exact_text('04 June,1991'))
    browser.all('.modal-body tr td')[11].should(have.exact_text('Maths'))
    browser.all('.modal-body tr td')[13].should(have.exact_text('Sports'))
    browser.all('.modal-body tr td')[15].should(have.exact_text('cat.jpg'))
    browser.all('.modal-body tr td')[17].should(have.exact_text('123 Street, City, Country'))
    browser.all('.modal-body tr td')[19].should(have.exact_text('NCR Delhi'))

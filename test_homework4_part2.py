from selenium import webdriver
from datetime import datetime
import pytest

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

# Тест регистрации на сайте
def test_registration(browser):
    browser.get("http://selenium1py.pythonanywhere.com/ru/")
    browser.find_element_by_css_selector("#login_link").click()
    mail_random = 'mail' + str(datetime.now().strftime('%H%M%S')) + '@auto.test'
    email_new = browser.find_element_by_css_selector("[name='registration-email']")
    email_new.send_keys(mail_random)
    pswd = "Qwe123rty_"
    password1 = browser.find_element_by_css_selector("[name='registration-password1']")
    password1.send_keys(pswd)
    password2 = browser.find_element_by_css_selector("[name='registration-password2']")
    password2.send_keys(pswd)
    browser.find_element_by_css_selector("[name='registration_submit']").click()
    message_register = browser.find_element_by_css_selector(".alertinner.wicon").text
    assert message_register == "Спасибо за регистрацию!"

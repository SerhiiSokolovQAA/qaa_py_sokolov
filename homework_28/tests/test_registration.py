import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPageLocators
from pages.registration_page import RegistrationPageLocators


@pytest.fixture
def open_registration(driver):
    driver.find_element(*MainPageLocators.SIGN_UP_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.FIRST_NAME)
    )


@pytest.fixture
def fill_registration_form(driver):
    def _fill(data):
        driver.find_element(*RegistrationPageLocators.FIRST_NAME).send_keys(data["first_name"])
        driver.find_element(*RegistrationPageLocators.LAST_NAME).send_keys(data["last_name"])
        driver.find_element(*RegistrationPageLocators.EMAIL).send_keys(data["email"])
        driver.find_element(*RegistrationPageLocators.PASSWORD).send_keys(data["password"])
        driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD).send_keys(data["password"])
    return _fill


@pytest.fixture
def submit_registration(driver):
    def _submit():
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.SUCCESS_MODAL)
        )
    return _submit


@pytest.fixture
def registration_data():
    return {
        "first_name": "Ivan",
        "last_name": "Petrenko",
        "email": f"test_{int(time.time())}@mail.com",
        "password": "Password1!"
    }


def test_user_registration(driver, open_registration, registration_data, fill_registration_form, submit_registration):
    open_registration

    fill_registration_form(registration_data)

    submit_registration()

    success_text = driver.find_element(*RegistrationPageLocators.SUCCESS_MODAL).text
    assert "success" in success_text.lower() or "registration" in success_text.lower()

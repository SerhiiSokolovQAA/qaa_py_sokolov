from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    FIRST_NAME = (By.ID, "signupName")
    LAST_NAME = (By.ID, "signupLastName")
    EMAIL = (By.ID, "signupEmail")
    PASSWORD = (By.ID, "signupPassword")
    REPEAT_PASSWORD = (By.ID, "signupRepeatPassword")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Register']")
    SUCCESS_MODAL = (By.CLASS_NAME, "modal-title")   # після реєстрації з'являється

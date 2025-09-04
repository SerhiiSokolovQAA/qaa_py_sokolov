import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield driver
    driver.quit()

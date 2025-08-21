from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class NovaPoshtaTracker:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)

    def open_site(self):
        self.driver.get("https://tracking.novaposhta.ua/#/uk")

    def track_parcel(self, tracking_number: str) -> str:
        input_field = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='en']"))
        )
        input_field.clear()
        input_field.send_keys(tracking_number)

        track_btn = self.driver.find_element(By.XPATH, "//*[@id='np-number-input-desktop-btn-search-en']")
        track_btn.click()

        status_elem = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.header__status-text"))
        )
        return status_elem.text

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    expected_status = "Посилка отримана"
    tracking_number = "123456789012"

    tracker = NovaPoshtaTracker()
    tracker.open_site()
    status = tracker.track_parcel(tracking_number)
    print("Status:", status)

    assert status == expected_status, f"Status '{status}' does not match with '{expected_status}'"

    tracker.close()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://localhost:8000/dz.html")

def verify_frame(frame_id, input_id, secret_text):
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, frame_id))
    )

    input_box = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, input_id))
    )
    input_box.clear()
    input_box.send_keys(secret_text)

    driver.find_element(By.TAG_NAME, "button").click()

    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = Alert(driver)
    alert_text = alert.text
    print(f"[{frame_id}] Alert text: {alert_text}")

    assert "успішно" in alert_text, f"Verification failed in {frame_id}"

    alert.accept()

    driver.switch_to.default_content()


verify_frame("frame1", "input1", "Frame1_Secret")

verify_frame("frame2", "input2", "Frame2_Secret")

print("All frames passed OK")

time.sleep(2)
driver.quit()

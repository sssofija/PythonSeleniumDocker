from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from utils.routes import get_url

class RadioButtonPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.URL = get_url("radio_button")

    def open(self):
        self.driver.get(self.URL)
        self.close_ad_if_present()

    def close_ad_if_present(self):
        try:
            ad = self.driver.find_element(By.ID, "close-fixedban")
            ad.click()
        except NoSuchElementException:
            pass

    def select_radio(self, option_text):
        label = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//label[contains(text(), '{option_text}')]")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", label)
        self.driver.execute_script("arguments[0].click();", label)

    def get_result_message(self):
        result = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "text-success")))
        return result.text.strip()

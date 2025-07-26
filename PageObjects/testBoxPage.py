import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.routes import get_url


class TextBoxPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open Text Box page")
    def open(self):
        self.driver.get(get_url("text_box"))

    @allure.step("Close advertisement if present")
    def close_ad_if_present(self):
        try:
            ad = self.driver.find_element(By.ID, "close-fixedban")
            ad.click()
        except Exception as e:
            pass

    @allure.step("Fill Full Name: {full_name}")
    def fill_full_name(self, full_name):
        elem = self.driver.find_element(By.ID, "userName")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        elem.clear()
        elem.send_keys(full_name)

    @allure.step("Fill Email: {email}")
    def fill_email(self, email):
        elem = self.driver.find_element(By.ID, "userEmail")
        elem.clear()
        elem.send_keys(email)

    @allure.step("Fill Current Address: {address}")
    def fill_current_address(self, address):
        elem = self.driver.find_element(By.ID, "currentAddress")
        elem.clear()
        elem.send_keys(address)

    @allure.step("Fill Permanent Address: {address}")
    def fill_permanent_address(self, address):
        elem = self.driver.find_element(By.ID, "permanentAddress")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        elem.clear()
        elem.send_keys(address)

    @allure.step("Submit the form")
    def submit_form(self):
        submit_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        self.close_ad_if_present()
        submit_btn.click()

    @allure.step("Get output data after form submission")
    def get_output_data(self):
        output_element = self.wait.until(EC.visibility_of_element_located((By.ID, "output")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", output_element)
        paragraphs = output_element.find_elements(By.CSS_SELECTOR, "p.mb-1")

        output_data = {}
        for p in paragraphs:
            text = p.text
            if ":" in text:
                key, value = text.split(":", 1)
                output_data[key.strip()] = value.strip()

        return output_data

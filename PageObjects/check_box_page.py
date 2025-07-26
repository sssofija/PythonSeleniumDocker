from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.routes import get_url


class CheckBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(get_url("checkbox"))

    def expand_all(self):
        expand_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Expand all']"))
        )
        expand_button.click()

    def click_home_checkbox(self):
        home_checkbox_label = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='tree-node-home']"))
        )
        home_checkbox_label.click()

    def get_selected_items(self):
        result_element = self.wait.until(EC.visibility_of_element_located((By.ID, "result")))
        selected_texts = result_element.find_elements(By.CSS_SELECTOR, "span.text-success")
        return [el.text.lower() for el in selected_texts]

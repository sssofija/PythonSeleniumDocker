import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.routes import get_url


class WebTablesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(get_url("webtables"))

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_add_button(self):
        add_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
        add_btn.click()

    def fill_form(self, first_name, last_name, email, age, salary, department):
        self.wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys(first_name)
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)
        self.driver.find_element(By.ID, "userEmail").send_keys(email)
        self.driver.find_element(By.ID, "age").send_keys(str(age))
        self.driver.find_element(By.ID, "salary").send_keys(str(salary))
        self.driver.find_element(By.ID, "department").send_keys(department)

    def fill_and_attach_user_data(self, user_data: dict):
        """Заполняет форму и прикрепляет тестовые данные в Allure."""
        self.fill_form(
            user_data["first_name"],
            user_data["last_name"],
            user_data["email"],
            user_data["age"],
            user_data["salary"],
            user_data["department"],
        )

        allure.attach(
            str(user_data),
            name="User Form Data",
            attachment_type=allure.attachment_type.JSON
        )

    def submit_form(self):
        submit_btn = self.driver.find_element(By.ID, "submit")
        submit_btn.click()

    def is_user_in_table(self, first_name, last_name, email):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "rt-table")))

        rows = self.driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        for row in rows:
            cells = row.find_elements(By.CLASS_NAME, "rt-td")
            if not cells:
                continue
            row_data = [cell.text.strip() for cell in cells]
            if first_name == row_data[0] and last_name == row_data[1] and email == row_data[3]:
                return True
        return False

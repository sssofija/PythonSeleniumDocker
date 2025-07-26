#allure serve allure-results
#pytest tests/test_1TextBox.py --alluredir=allure-results

from PageObjects.testBoxPage import *
from utils.fake_data import generate_user_data

@allure.feature("Text Box")
@allure.story("Fill and submit form")
def test_text_box_form(browser):
    user_data = generate_user_data()

    page = TextBoxPage(browser)
    page.open()
    page.close_ad_if_present()

    with allure.step("Fill Full Name"):
        page.fill_full_name(user_data["full_name"])

    with allure.step("Fill Email"):
        page.fill_email(user_data["email"])

    with allure.step("Fill Current Address"):
        page.fill_current_address(user_data["current_address"])

    with allure.step("Fill Permanent Address"):
        page.fill_permanent_address(user_data["permanent_address"])

    page.close_ad_if_present()

    with allure.step("Submit the form"):
        page.submit_form()

    with allure.step("Verify output displays correct data"):
        output = page.get_output_data()
        assert output.get("Name") == user_data["full_name"]
        assert output.get("Email") == user_data["email"]
        assert output.get("Current Address") == user_data["current_address"]
        assert output.get("Permananet Address") == user_data["permanent_address"]

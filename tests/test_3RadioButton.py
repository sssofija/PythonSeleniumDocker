#allure serve allure-results
#pytest tests/test_3RadioButton.py --alluredir=allure-results

import allure
from PageObjects.radio_button_page import RadioButtonPage

@allure.feature("Radio Button")
@allure.story("Select Yes and Impressive options and verify result messages")
def test_radio_buttons(browser):
    page = RadioButtonPage(browser)
    page.open()

    with allure.step("Select 'Yes' radio button"):
        page.select_radio("Yes")
        message = page.get_result_message()

        allure.attach("Yes", name="Selected Option", attachment_type=allure.attachment_type.TEXT)
        allure.attach(message, name="Displayed Message", attachment_type=allure.attachment_type.TEXT)

        assert message == "Yes", f"Expected message 'Yes', got '{message}'"

    with allure.step("Select 'Impressive' radio button"):
        page.select_radio("Impressive")
        message = page.get_result_message()

        allure.attach("Impressive", name="Selected Option", attachment_type=allure.attachment_type.TEXT)
        allure.attach(message, name="Displayed Message", attachment_type=allure.attachment_type.TEXT)

        assert message == "Impressive", f"Expected message 'Impressive', got '{message}'"

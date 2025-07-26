#allure serve allure-results
#pytest tests/test_5WebTables.py --alluredir=allure-results


import allure
from PageObjects.web_tables_page import WebTablesPage
from utils.fake_data import generate_webtable_user_data


@allure.feature("Web Tables")
@allure.story("Add a user and verify it appears in the table")
def test_add_user_to_web_table(browser):
    user = generate_webtable_user_data()
    page = WebTablesPage(browser)
    page.open()

    with allure.step("Scroll down to the Add button"):
        page.scroll_to_bottom()

    with allure.step("Click Add button"):
        page.click_add_button()

    with allure.step("Fill in the form with generated user data"):
        if hasattr(page, "fill_and_attach_user_data"):
            page.fill_and_attach_user_data(user)
        else:
            page.fill_form(
                first_name=user["first_name"],
                last_name=user["last_name"],
                email=user["email"],
                age=user["age"],
                salary=user["salary"],
                department=user["department"]
            )
            allure.attach(
                str(user),
                name="User Test Data",
                attachment_type=allure.attachment_type.JSON
            )

    with allure.step("Submit the form"):
        page.submit_form()

    with allure.step("Verify the user appears in the table"):
        assert page.is_user_in_table(
            user["first_name"], user["last_name"], user["email"]
        ), "User not found in table"

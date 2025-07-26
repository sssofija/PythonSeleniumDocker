#allure serve allure-results
#pytest tests/test_2CheckBox.py --alluredir=allure-results

import allure
from PageObjects.check_box_page import CheckBoxPage

@allure.feature("Check Box")
@allure.story("Select Home checkbox and verify all nested are selected")
def test_check_home_checkbox_selects_all_nested(browser):
    page = CheckBoxPage(browser)

    with allure.step("Open Check Box page"):
        page.open()

    with allure.step("Wait and expand all nodes"):
        page.expand_all()

    with allure.step("Click Home checkbox to select all nested items"):
        page.click_home_checkbox()

    with allure.step("Retrieve all selected items from result section"):
        selected_items = page.get_selected_items()

    expected_items = [
        "home",
        "desktop",
        "notes",
        "commands",
        "documents",
        "workspace",
        "react",
        "angular",
        "veu",
        "office",
        "public",
        "private",
        "classified",
        "general"
    ]

    with allure.step("Verify that all expected items are selected"):
        for item in expected_items:
            assert item in selected_items, f"Item '{item}' should be selected but is not."

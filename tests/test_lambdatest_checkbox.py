from page_objects.lambdatest_home_page import LambdaTestHomePage

def test_checkbox_interaction(driver):
    home_page = LambdaTestHomePage(driver)
    home_page.navigate_to_home()
    home_page.wait_for_dom_ready()

    checkbox_parent = home_page.get_weekday_checkbox_parent()
    checkbox_input = home_page.get_weekday_checkbox_input(checkbox_parent)
    checkmark = home_page.get_checkmark_span(checkbox_parent)

    initial_state = home_page.get_initial_checkbox_state(checkbox_input)
    print(f"Initial state of weekday checkbox: {initial_state}")

    home_page.click_checkmark(checkmark)
    home_page.wait_for_checkbox_state_change(checkbox_input, initial_state)

    final_state = home_page.get_final_checkbox_state(checkbox_input)
    print(f"Final state of weekday checkbox: {final_state}")

    assert initial_state != final_state, "Checkbox state should have changed."

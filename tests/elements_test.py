import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage

url_textbox = 'https://demoqa.com/text-box'
url_checkbox = 'https://demoqa.com/checkbox'
url_radiobutton = 'https://demoqa.com/radio-button'


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, url_textbox)
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_address, output_perm_address = text_box_page.check_filled_form()
            assert full_name == output_name, 'Full name not match '
            assert email == output_email, 'Email not match'
            assert current_address == output_curr_address, 'Current address not match'
            assert permanent_address == output_perm_address, 'Permanent address not match'

    class TestCheckbox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, url_checkbox)
            check_box_page.open()
            check_box_page.expand_checkbox_lict()
            check_box_page.collapse_checkbox_list()
            check_box_page.expand_checkbox_lict()
            check_box_page.click_random_checkbox()
            checked_list = check_box_page.get_checked_list()
            output_list = check_box_page.get_output_result()

            assert checked_list == output_list, 'Checked list is not correct'

    class TestRadioButton:
        @pytest.mark.xfail
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, url_radiobutton)
            radio_button_page.open()
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', 'Radio_Yes was not selected'
            assert output_impressive == 'Impressive', 'Radio_Impressive was not selected'
            assert output_no == 'No', 'Radio_No was not selected'

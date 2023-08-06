import random
import time

import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage

url_textbox = 'https://demoqa.com/text-box'
url_checkbox = 'https://demoqa.com/checkbox'
url_radiobutton = 'https://demoqa.com/radio-button'
url_webtable = 'https://demoqa.com/webtables'


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

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, url_webtable)
            web_table_page.open()
            input_list = web_table_page.add_new_person(random.randint(1, 5))
            output_list = web_table_page.get_full_persons_list()
            for input_item in input_list:
                assert input_item in output_list, 'List of new persons is Not correct'

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, url_webtable)
            web_table_page.open()
            web_table_page.add_new_person(random.randint(1, 5))
            output_list = web_table_page.get_full_persons_list()
            # определяем количество заполненных строк
            empty_row_qty = web_table_page.get_empty_row_qty()
            output_list_qty = len(output_list)
            filled_row_qty = output_list_qty - empty_row_qty - 1

            # случайный критерий для поиска
            key_word = output_list[random.randint(0, filled_row_qty)][random.randint(0, 5)]
            web_table_page.search_person(key_word)
            search_result = web_table_page.get_search_person()
            assert key_word in search_result, ''

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, url_webtable)
            web_table_page.open()
            last_name = web_table_page.add_new_person()[0][1]
            web_table_page.search_person(last_name)
            age = web_table_page.update_person_info()
            row = web_table_page.get_search_person()
            assert age in row, 'The person info was not updated'





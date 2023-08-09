import random

import pytest
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    DownUploadPage, DynamicPropsPage

url_textbox = 'https://demoqa.com/text-box'
url_checkbox = 'https://demoqa.com/checkbox'
url_radiobutton = 'https://demoqa.com/radio-button'
url_webtable = 'https://demoqa.com/webtables'
url_buttons = 'https://demoqa.com/buttons'
url_links = 'https://demoqa.com/links'
url_down_upload = 'https://demoqa.com/upload-download'
url_dynamic = 'https://demoqa.com/dynamic-properties'


class TestElements:
    class TestTextBox:
        @pytest.mark.test
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

        def test_delete_person(self, driver):
            web_table_page = WebTablePage(driver, url_webtable)
            web_table_page.open()
            email = web_table_page.add_new_person()[0][3]
            web_table_page.search_person(email)
            web_table_page.delete_person()
            text = web_table_page.get_delete_confirmation()
            assert text == 'No rows found', ''

        @pytest.mark.xfail
        def test_web_table_rows_per_page(self, driver):
            web_table_page = WebTablePage(driver, url_webtable)
            web_table_page.open()
            data, count = web_table_page.change_rows_count()
            assert data == count, "oops, It's not possible to choose 5, 10, 20, 25 rows per page"
            # для строк 50 и 100
            data1, count1 = web_table_page.change_rows_count_fail()
            assert data1 == count1, "oops, It's not possible to choose 50 and 100 rows per page"

    class TestButtonsPage:
        def test_different_click_on_the_button(self, driver):
            buttons_page = ButtonsPage(driver, url_buttons)
            buttons_page.open()
            double = buttons_page.click_on_different_button('double')
            right = buttons_page.click_on_different_button('right')
            click = buttons_page.click_on_different_button('click')

            assert double == 'You have done a double click', 'Double-click button was not pressed'
            assert right == 'You have done a right click', 'Right-click button was not pressed'
            assert click == 'You have done a dynamic click', 'Dynamic button was not pressed'

    class TestLinksPage:
        def test_new_tab_link(self, driver):
            links_page = LinksPage(driver, url_links)
            links_page.open()
            href, new_tab = links_page.check_new_tab_link('simple')
            assert href == new_tab, 'Bad request'
            href, new_tab = links_page.check_new_tab_link('dynamic')
            assert href == new_tab, 'bad request'

        def test_api_link(self, driver):
            links_page = LinksPage(driver, url_links)
            links_page.open()
            for i in range(2, 9):
                name_link, request, code, status = links_page.check_api_link(i)
                assert code == str(request), 'Bad request to API'

    class TestDownUploadFile:
        def test_upload_file(self, driver):
            down_upload_page = DownUploadPage(driver, url_down_upload)
            down_upload_page.open()
            name, message = down_upload_page.upload_file()
            assert name == message, 'The File was not upload'

        def test_download_file(self, driver):
            down_upload_page = DownUploadPage(driver, url_down_upload)
            down_upload_page.open()
            check_file = down_upload_page.download_file()
            assert check_file, 'The File was not download'

    class TestDynamicPropsPage:
        def test_dynamic_text(self, driver):
            dynamic_page = DynamicPropsPage(driver, url_dynamic)
            dynamic_page.open()
            text_id_1, text_id_2 = dynamic_page.get_text_id()
            assert text_id_1 != text_id_2, "The element ID is not dynamic"

        def test_enable_button(self, driver):
            dynamic_page = DynamicPropsPage(driver, url_dynamic)
            dynamic_page.open()
            enable_click = dynamic_page.enable_button()
            assert enable_click, 'The button is not enable/clickable'

        def test_color_change(self, driver):
            dynamic_page = DynamicPropsPage(driver, url_dynamic)
            dynamic_page.open()
            color_button_before, color_button_after = dynamic_page.color_change()
            assert color_button_before != color_button_after, 'Color was not changed'

        def test_visible_button(self, driver):
            dynamic_page = DynamicPropsPage(driver, url_dynamic)
            dynamic_page.open()
            appeared = dynamic_page.visible_button()
            assert appeared, 'The alert is not appeared'

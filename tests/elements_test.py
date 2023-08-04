import time
from pages.elements_page import TextBoxPage

url = 'https://demoqa.com/text-box'


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_address, output_perm_address = text_box_page.check_filled_form()
            assert full_name == output_name, 'Full name not match '
            assert email == output_email, 'Email not match'
            assert current_address == output_curr_address, 'Current address not match'
            assert permanent_address == output_perm_address, 'Permanent address not match'

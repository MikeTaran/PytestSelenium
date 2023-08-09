import random
import time

import pytest
from pages.forms_page import FormsPage

url_forms = 'https://demoqa.com/automation-practice-form'


class TestForms:
    class TestPracticeForm:
        @pytest.mark.test
        def test_text_box(self, driver):
            forms_page = FormsPage(driver, url_forms)
            forms_page.open()
            forms_page.fill_static_fields()
            radio_btn_name = forms_page.fill_gender_radiobutton()
            # forms_page.fill_date_of_birth()
            forms_page.fill_hobbies_checkboxes()
            picture_name = forms_page.upload_picture()
            print(radio_btn_name)
            print(picture_name)
            time.sleep(10)

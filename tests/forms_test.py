import random
import time

import pytest
from pages.forms_page import FormsPage

url_forms = 'https://demoqa.com/automation-practice-form'


class TestForms:
    class TestPracticeForm:
        @pytest.mark.test
        def test_text_box(self, driver):
            input_data = []
            forms_page = FormsPage(driver, url_forms)
            forms_page.open()
            full_name, email, mobile, current_address = forms_page.fill_static_fields()
            radio_btn_name = forms_page.fill_gender_radiobutton()
            # forms_page.fill_date_of_birth()
            # forms_page.fill_subject_field()
            forms_page.fill_hobbies_checkboxes()
            picture_name = forms_page.upload_picture()
            forms_page.fill_state_and_city_fields()
            #
            forms_page.submit_input()
            assert forms_page.check_submitted_form_present(), 'The submitted form isNot present'
            #
            submitted_data = forms_page.get_submitted_data()
            print(full_name, email, mobile, current_address)
            print(radio_btn_name)
            print(picture_name)
            print(submitted_data)

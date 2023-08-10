import pytest
from pages.forms_page import FormsPage

url_forms = 'https://demoqa.com/automation-practice-form'


class TestForms:
    class TestPracticeForm:
        @pytest.mark.test
        def test_text_box(self, driver):
            forms_page = FormsPage(driver, url_forms)
            forms_page.open()
            full_name, email, mobile, current_address = forms_page.fill_static_fields()
            gender = forms_page.fill_gender_radiobutton()
            date_of_birth = forms_page.fill_date_of_birth()
            subject = forms_page.fill_subject_field()
            hobbies = forms_page.fill_hobbies_checkboxes()
            picture_name = forms_page.upload_picture()
            state_city = forms_page.fill_state_and_city_fields()
            #
            forms_page.check_submit_button()
            assert forms_page.check_submitted_form_present(), 'The submitted form isNot present'
            #
            input_data = [full_name, email, gender, str(mobile), date_of_birth, subject, hobbies, picture_name,
                          current_address, state_city]
            submitted_data = forms_page.get_submitted_data()
            forms_page.check_close_button()
            assert forms_page.check_submitted_form_not_present(), 'The submitted form is present'
            print('\n')
            print(input_data)
            print(submitted_data)
            for i in range(len(submitted_data)):
                try:
                    assert input_data[i] == submitted_data[i], f'InputData: {input_data[i]} is not match'
                except AssertionError:
                    print(f'InputData: {input_data[i]} is not match')


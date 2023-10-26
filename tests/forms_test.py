import allure
import pytest
from pages.forms_page import FormsPage

url_forms = 'https://demoqa.com/automation-practice-form'


@allure.suite('Forms')
class TestForms:
    @allure.feature('Test Practice Form')
    class TestPracticeForm:
        @pytest.mark.xfail
        @allure.title('Check practice form')
        def test_practice_form(self, driver):
            forms_page = FormsPage(driver, url_forms)
            forms_page.open()
            with allure.step('Filing person data'):
                full_name, email, mobile, current_address = forms_page.fill_static_fields()
                gender = forms_page.fill_gender_radiobutton()
                date_of_birth = forms_page.fill_date_of_birth()
                subject = forms_page.fill_subject_field()
                hobbies = forms_page.fill_hobbies_checkboxes()
                picture_name = forms_page.upload_picture()
                state_city = forms_page.fill_state_and_city_fields()
                forms_page.allure_screenshot()
            #
            forms_page.check_submit_button()
            with allure.step('assert form present'):
                assert forms_page.check_submitted_form_present(), 'The submitted form isNot present'
            #
            input_data = [full_name, email, gender, str(mobile), date_of_birth, subject, hobbies, picture_name,
                          current_address, state_city]
            with allure.step('Get submitted data'):
                submitted_data = forms_page.get_submitted_data()
                forms_page.allure_screenshot()
            forms_page.check_close_button()
            with allure.step('assert form not present'):
                assert forms_page.check_submitted_form_not_present(), 'The submitted form is present'
            with allure.step('assert check filling form'):
                for i in range(len(submitted_data)):
                    assert input_data[i] == submitted_data[i], f'InputData: {input_data[i]} is not match'

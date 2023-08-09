import random
import pytest
from pages.forms_page import FormsPage

url_forms = 'https://demoqa.com/automation-practice-form'


class TestForms:
    class TestPracticeForm:
        @pytest.mark.test
        def test_text_box(self, driver):
            forms_page = FormsPage(driver, url_forms)
            forms_page.open()

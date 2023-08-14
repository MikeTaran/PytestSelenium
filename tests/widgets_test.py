import random

import pytest

from pages.widgets_page import AccordianWidgetsPage, AutoCompletePage, DatePickerPage, SliderPage

url_accordian = 'https://demoqa.com/accordian'
url_autocomplete = 'https://demoqa.com/auto-complete'
url_date = 'https://demoqa.com/date-picker'
url_slider = 'https://demoqa.com/slider'
url_bar = 'https://demoqa.com/progress-bar'
url_tabs = 'https://demoqa.com/tabs'
url_tooltips = 'https://demoqa.com/tool-tips'
url_menu = 'https://demoqa.com/menu'
url_select_menu = 'https://demoqa.com/select-menu'


class TestWidgets:
    class TestAccordian:
        def test_accordian(self, driver):
            widget_page = AccordianWidgetsPage(driver, url_accordian)
            widget_page.open()
            accordian_len, title, content, accord = widget_page.check_accordian_content()
            title_mockup = ['What is Lorem Ipsum?', 'Where does it come from?', 'Why do we use it?']
            for i in range(accordian_len):
                assert content[i] != 0, f'The block_{i} is empty'
                assert title[i] == title_mockup[i], f'The title of block_{i} is Not correct'
            assert accord, 'More than one block was opened'

    class TestAutoComplete:
        input_letter = 'qwertyuiopadghklcvbnm'
        color_data = ["Aqua", "Magenta", "Indigo", "Voilet", "White", "White", "Black", "Purple",
                      "Yellow", "Green", "Blue", "Red"]

        def test_multy_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, url_autocomplete)
            autocomplete_page.open()
            num = random.randint(1, 10)
            lst_letters = random.sample(self.input_letter, k=num)
            #
            data = autocomplete_page.check_multy_input(lst_letters)
            for color in data:
                assert color in self.color_data, f'The color: {color} is Not in colors list'

        def test_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, url_autocomplete)
            autocomplete_page.open()
            rnd_letter = random.sample(self.input_letter, k=1)
            # rnd_letter = self.input_letter[random.randint(0, len(self.input_letter) - 1)]
            color = autocomplete_page.check_single_input(*rnd_letter)
            assert color in self.color_data, f'The color: {color} is Not in colors list'

        def test_multy_element_deletion(self, driver):
            autocomplete_page = AutoCompletePage(driver, url_autocomplete)
            autocomplete_page.open()
            input_list, output_list = autocomplete_page.check_multy_element_deletion()
            assert input_list - output_list == 1, 'It was deleted more or less one items'

        def test_all_multy_deletion(self, driver):
            autocomplete_page = AutoCompletePage(driver, url_autocomplete)
            autocomplete_page.open()
            result_list = autocomplete_page.test_all_multy_deletion()
            assert result_list, 'Not all colors were deleted'

    class TestDatePicker:

        @pytest.mark.xfail
        def test_only_full_date_picker(self, driver):
            date_picker_page = DatePickerPage(driver, url_date)
            date_picker_page.open()
            input_date, output_date = date_picker_page.check_only_date_picker_input_fulldate()
            assert input_date == output_date, ''

        def test_only_separate_data_picker(self, driver):
            date_picker_page = DatePickerPage(driver, url_date)
            date_picker_page.open()
            input_date, output_date = date_picker_page.check_separate_data_input()
            assert input_date == output_date, ''

        @pytest.mark.xfail
        def test_date_and_time_picker(self, driver):
            date_picker_page = DatePickerPage(driver, url_date)
            date_picker_page.open()
            input_date, output_date = date_picker_page.check_date_and_time_input()
            assert input_date == output_date, ''

        def test_date_time_separate_input_picker(self, driver):
            date_picker_page = DatePickerPage(driver, url_date)
            date_picker_page.open()
            start_date, input_date, output_date = date_picker_page.check_date_and_time_separate_input()
            assert start_date != input_date == output_date, ''

    class TestSlider:
        def test_slider(self, driver):
            slider_page = SliderPage(driver, url_slider)
            slider_page.open()
            slider_page.check_slider()
            value_before, value_after = slider_page.check_slider()
            print(value_before, value_after)

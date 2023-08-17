import random

import pytest

from pages.widgets_page import AccordianWidgetsPage, AutoCompletePage, DatePickerPage, SliderPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage

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
            assert input_date == output_date, 'The date was Not changed, after full date input'

        def test_only_separate_data_picker(self, driver):
            date_picker_page = DatePickerPage(driver, url_date)
            date_picker_page.open()
            input_date, output_date = date_picker_page.check_separate_data_input()
            assert input_date == output_date, 'The date was Not changed, after separate date input'

        @pytest.mark.xfail
        def test_date_and_time_picker(self, driver):
            date_picker_page = DatePickerPage(driver, url_date)
            date_picker_page.open()
            input_date, output_date = date_picker_page.check_date_and_time_input()
            assert input_date == output_date, 'The date was Not changed, after full date input'

        def test_date_time_separate_input_picker(self, driver):
            date_picker_page = DatePickerPage(driver, url_date)
            date_picker_page.open()
            start_date, input_date, output_date = date_picker_page.check_date_and_time_separate_input()
            assert start_date != input_date == output_date, ('The date and time were Not changed,'
                                                             ' after separate date input')

    class TestSlider:
        def test_slider(self, driver):
            slider_page = SliderPage(driver, url_slider)
            slider_page.open()
            value_before, value_after = slider_page.check_slider()
            assert value_before != value_after, 'The slider value has Not been changed'

        def test_progressive_bar(self, driver):
            slider_page = SliderPage(driver, url_bar)
            slider_page.open()
            value_before, value_after, start, stop = slider_page.check_progress_bar()

            assert start == 'Start' and stop == 'Stop', 'The name of button has Not been changed'
            if value_after == '100%':
                assert value_before == value_after, 'The reset button is Not pressed'
            else:
                assert value_before != value_after, 'The progress bar is Not changed'

    class TestTabs:
        @pytest.mark.xfail
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, url_tabs)
            tabs_page.open()
            assert_rez, title_list, content_list = tabs_page.check_tabs()

            for i in range(len(content_list)):
                assert content_list[i] > 0, f'The tab "{title_list[i]}" is empty.'
            assert assert_rez, 'Some tab is Not clickable'

    class TestToolTips:
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, url_tooltips)
            tool_tips_page.open()
            (tooltip_button, tooltip_text_field, tooltip_contrary_text,
             tooltip_numbers_text) = tool_tips_page.check_tool_tips()

            assert tooltip_button == 'You hovered over the Button', f'Hover was missed: {tooltip_button}'
            assert tooltip_text_field == 'You hovered over the text field', f'Hover was missed: {tooltip_text_field}'
            assert tooltip_contrary_text == 'You hovered over the Contrary', \
                f'Hover was missed: {tooltip_contrary_text}'
            assert tooltip_numbers_text == 'You hovered over the 1.10.32', f'Hover was missed: {tooltip_numbers_text}'

    class TestMenu:
        def test_menu(self, driver):
            mockup_title = ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »',
                            'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']
            menu_page = MenuPage(driver, url_menu)
            menu_page.open()
            menu_title = menu_page.check_menu()
            assert mockup_title == menu_title, 'Menu is Not match mockup'

    class TestSelectMenu:
        def test_select_value_dropdown(self, driver):
            select_menu_page = SelectMenuPage(driver, url_select_menu)
            select_menu_page.open()
            text_before, text_after = select_menu_page.check_select_value_dropdown()
            assert text_before != text_after, 'The value was Not selected'

        def test_select_one_dropdown(self, driver):
            select_menu_page = SelectMenuPage(driver, url_select_menu)
            select_menu_page.open()
            text_before, text_after = select_menu_page.check_select_one_dropdown()
            assert text_before != text_after, 'The value was Not selected'

        def test_old_stile_menu(self, driver):
            select_menu_page = SelectMenuPage(driver, url_select_menu)
            select_menu_page.open()
            text_before, text_after = select_menu_page.check_old_stile_menu()
            assert text_before != text_after, 'The value was Not selected'

        def test_multy_dropdown(self, driver):
            select_menu_page = SelectMenuPage(driver, url_select_menu)
            select_menu_page.open()
            test = select_menu_page.check_multy_dropdown()
            assert test == 1, 'The value was Not selected'

        def test_standard_multiselect(self, driver):
            select_menu_page = SelectMenuPage(driver, url_select_menu)
            select_menu_page.open()
            test = select_menu_page.check_standard_multiselect()
            assert test, 'The value was Not selected'

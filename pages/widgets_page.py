import calendar
import random
import time

import allure
from selenium.webdriver.common.by import By

from generator.generator import generate_random_date as rnd_date, convert_to_12_hour_format as conv_12h

from selenium.common import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

from locators.widgets_page_locators import AccordianWidgetsPageLocators, AutoCompletePageLocators, \
    DatePickerPageLocators, SliderPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SelectMenuPageLocators
from pages.base_page import BasePage


class AccordianWidgetsPage(BasePage):
    locators = AccordianWidgetsPageLocators()

    @allure.step('check_accordian_content')
    def check_accordian_content(self):
        title_data = []
        content_len_data = []
        accord_data = True
        accordian_len = len(self.elements_are_present(self.locators.ACCORDIAN_LIST))
        title_list = self.elements_are_visible(self.locators.ACCORDIAN_TITLE_LIST)
        content_list = self.elements_are_present(self.locators.ACCORDIAN_CONTENT_LIST)
        for i in range(accordian_len):

            title_data.append(title_list[i].text)
            title_list[i].click()
            time.sleep(0.2)
            content = len(content_list[i].text)
            if content == 0:
                title_list[i].click()
                time.sleep(0.2)
                content = len(content_list[i].text)
            content_len_data.append(content)
            # проверка, что одновременно открыта только одна вкладка
            for j in range(accordian_len):
                if j != i:
                    cont = len(content_list[j].text)
                    if cont != 0:
                        accord_data = False

        return accordian_len, title_data, content_len_data, accord_data


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    @allure.step('check_multy_input')
    def check_multy_input(self, input_list):
        data = []
        multy_input = self.element_is_visible(self.locators.MULTY_INPUT)
        for inp in input_list:
            multy_input.clear()
            multy_input.send_keys(inp)
            multy_input.send_keys(Keys.RETURN)
        result_list = self.elements_are_visible(self.locators.MULTY_INPUT_RESULT_LIST)
        multy_input.clear()
        for result in result_list:
            data.append(result.text)
        return data

    @allure.step('check_single_input')
    def check_single_input(self, letter):
        single_input = self.element_is_visible(self.locators.SINGLE_INPUT)
        single_input.send_keys(letter)
        single_input.send_keys(Keys.RETURN)
        result = self.element_is_visible(self.locators.SINGLE_INPUT_RESULT).text
        return result

    @allure.step('check_multy_element_deletion')
    def check_multy_element_deletion(self):
        result = self.check_multy_input(['a', 'b', 'q', 'w'])
        index = random.randint(0, 3)
        delete_cross = self.elements_are_visible(self.locators.REMOVE_MULTY_ELEMENT)
        delete_cross[index].click()
        result_list = self.elements_are_visible(self.locators.MULTY_INPUT_RESULT_LIST)
        return len(result), len(result_list)

    @allure.step('test_all_multy_deletion')
    def test_all_multy_deletion(self):
        self.check_multy_input(['a', 'b', 'q', 'w'])
        all_delete_cross = self.element_is_visible(self.locators.REMOVE_ALL_MULTY_ELEMENT)
        all_delete_cross.click()
        try:
            self.element_is_not_visible(self.locators.MULTY_INPUT_RESULT_LIST)
            return True
        except TimeoutException:
            return False


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    @allure.step('check_only_date_picker_input_fulldate')
    def check_only_date_picker_input_fulldate(self):
        day, month, year, hour, minute = rnd_date()
        input_date = f'{month:02d}/{day:02d}/{year}'

        input_field = self.element_is_visible(self.locators.ONLY_DATE_INPUT)
        input_field.click()
        self.driver.execute_script("window.navigator.clipboard.writeText(arguments[0])", input_date)
        input_field.send_keys(Keys.CONTROL, 'a')
        input_field.send_keys(Keys.CONTROL, 'v')
        input_field.send_keys(Keys.RETURN)

        output_date = input_field.get_attribute('value')

        return input_date, output_date

    @allure.step('check_separate_data_input')
    def check_separate_data_input(self):
        day, month, year, hour, minute = rnd_date()
        input_date = f'{month:02d}/{day:02d}/{year}'
        input_field = self.element_is_visible(self.locators.ONLY_DATE_INPUT)
        input_field.click()
        select_month = Select(self.find_element(self.locators.ONLY_DATE_MONTH_INPUT_SELECT))
        select_month.select_by_value(str(month - 1))
        select_year = Select(self.find_element(self.locators.ONLY_DATE_YEAR_INPUT_SELECT))
        select_year.select_by_value(str(year))
        day_list = self.elements_are_visible(self.locators.ONLY_DATE_DAY_INPUT_LIST)
        for i in range(len(day_list) - 1):
            if day_list[i].text == '1':
                day_list[i + day - 1].click()
                break
        output_date = input_field.get_attribute('value')
        return input_date, output_date

    @allure.step('check_date_and_time_input')
    def check_date_and_time_input(self):
        day, month, year, hour, minute = rnd_date()
        month_name = calendar.month_name[month]
        input_date = f"{month_name} {day}, {year} 4:00 PM"

        input_field = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        input_field.click()
        self.driver.execute_script("window.navigator.clipboard.writeText(arguments[0])", input_date)
        input_field.send_keys(Keys.CONTROL, 'a')
        input_field.send_keys(Keys.CONTROL, 'v')
        input_field.send_keys(Keys.RETURN)

        output_date = input_field.get_attribute('value')
        return input_date, output_date

    @allure.step('check_date_and_time_separate_input')
    def check_date_and_time_separate_input(self):
        day, month, year, hour, minute = rnd_date()
        month_name = calendar.month_name[month]
        input_time = f'{hour:02d}:{minute:02d}'
        convert_time = conv_12h(input_time)
        input_date = f"{month_name} {day}, {year} {convert_time}"

        input_field = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        start_date = input_field.get_attribute('value')
        input_field.click()

        self.element_is_visible(self.locators.DATE_TIME_MONTH_INPUT).click()
        month_list = self.elements_are_visible(self.locators.DATE_TIME_MONTH_INPUT_LIST)
        month_list[month - 1].click()

        self.element_is_visible(self.locators.DATE_TIME_YEAR_INPUT).click()
        year_list = self.elements_are_present(self.locators.DATE_TIME_YEAR_INPUT_LIST)
        nav_arrow_list = self.elements_are_visible(self.locators.DATE_TIME_YEAR_NAVIGATION_ARROW)
        nav_arrow_up = nav_arrow_list[0]
        nav_arrow_down = nav_arrow_list[1]
        first_year = int(year_list[1].text)
        last_year = int(year_list[-2].text)

        if last_year <= year <= first_year:
            for new_year in year_list:
                if new_year.text == str(year):
                    new_year.click()
                    break

        if year > first_year:
            while year != first_year:
                nav_arrow_up.click()
                year_list = self.elements_are_present(self.locators.DATE_TIME_YEAR_INPUT_LIST)
                first_year = int(year_list[1].text)
            year_list[0].click()

        if year < last_year:
            while year != last_year:
                nav_arrow_down.click()
                year_list = self.elements_are_present(self.locators.DATE_TIME_YEAR_INPUT_LIST)
                last_year = int(year_list[-2].text)
            year_list[-2].click()

        day_list = self.elements_are_visible(self.locators.ONLY_DATE_DAY_INPUT_LIST)
        for i in range(len(day_list)):
            if day_list[i].text == '1':
                day_list[i + day - 1].click()
                break

        time_list = self.elements_are_present(self.locators.DATE_TIME_TIME_INPUT_LIST)
        for new_time in time_list:
            if new_time.text == input_time:
                new_time.click()
                break
        #
        output_date = input_field.get_attribute('value')
        return start_date, input_date, output_date


class SliderPage(BasePage):
    locators = SliderPageLocators()

    @allure.step('check_slider')
    def check_slider(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after

    @allure.step('check_progress_bar')
    def check_progress_bar(self):
        value_bar = self.element_is_present(self.locators.PROGRESSIVE_BAR_VALUE)
        value_before = value_bar.text
        start_stop_button = self.element_is_present(self.locators.PROGRESSIVE_BAR_START_BUTTON)
        start_button_name = start_stop_button.text
        start_stop_button.click()
        time.sleep(random.randint(2, 15))
        stop_button_name = start_stop_button.text
        try:
            reset_button = self.element_is_visible(self.locators.PROGRESSIVE_BAR_RESET_BUTTON, 0)
            reset_button.click()
        except TimeoutException:
            start_stop_button.click()
        value_after = value_bar.text
        return value_before, value_after, start_button_name, stop_button_name


class TabsPage(BasePage):
    locators = TabsPageLocators()

    @allure.step('check_tabs')
    def check_tabs(self):
        tabs_list = self.elements_are_present(self.locators.TABS_LIST)
        data_title = []
        data_content = []
        assert_rez = True
        for tab in tabs_list:
            data_title.append(tab.text)
            try:
                tab.click()
                tab_content = len(self.element_is_visible(self.locators.TAB_CONTENT).text)
                data_content.append(tab_content)
            except ElementClickInterceptedException:
                data_content.append(0)
                print(f'Tab: "{tab.text}" is Not clickable')
                assert_rez = False

        return assert_rez, data_title, data_content


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    @allure.step('get_text_from_tooltip')
    def get_text_from_tooltip(self, hover_element, hover_indicator):
        element = self.element_is_visible(hover_element)
        self.action_move_to_element(element)
        self.element_is_visible(hover_indicator)
        time.sleep(0.5)
        tooltips_text = self.element_is_visible(self.locators.HOVER_TOOLTIP).text
        return tooltips_text

    @allure.step('check_tool_tips')
    def check_tool_tips(self):
        tooltip_button = self.get_text_from_tooltip(self.locators.HOVER_BUTTON, self.locators.BUTTON_TOOLTIP)
        tooltip_text_field = self.get_text_from_tooltip(self.locators.INPUT_FIELD, self.locators.INPUT_FIELD_TOOLTIP)
        tooltip_contrary_text = self.get_text_from_tooltip(self.locators.CONTRARY_TEXT,
                                                           self.locators.CONTRARY_TEXT_TOOLTIP)
        tooltip_numbers_text = self.get_text_from_tooltip(self.locators.NUMBER_TEXT, self.locators.NUMBER_TEXT_TOOLTIP)

        return tooltip_button, tooltip_text_field, tooltip_contrary_text, tooltip_numbers_text


class MenuPage(BasePage):
    locators = MenuPageLocators()

    @allure.step('check_menu')
    def check_menu(self):
        data = []
        menu_list = self.elements_are_present(self.locators.MAIN_ITEM_LIST)
        for menu in menu_list:
            self.action_move_to_element(menu)
            data.append(menu.text)
        return data


class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    @allure.step('check_select_value_dropdown')
    def check_select_value_dropdown(self):
        select_value = self.element_is_visible(self.locators.SELECT_VALUE)
        text_before = select_value.text
        select_value.click()
        select_value_input = self.element_is_present(self.locators.SELECT_VALUE_INPUT)
        select_value_input.send_keys('g')
        select_value_input.send_keys(Keys.RETURN)
        text_after = self.element_is_visible(self.locators.SELECT_VALUE_TEXT).text
        return text_before, text_after

    @allure.step('check_select_one_dropdown')
    def check_select_one_dropdown(self):
        select_one = self.element_is_visible(self.locators.SELECT_ONE)
        text_before = select_one.text
        select_one.click()
        value_list = self.elements_are_present(self.locators.SELECT_ONE_INPUT_LIST)
        value_list[random.randint(0, len(value_list) - 1)].click()
        text_after = self.element_is_visible(self.locators.SELECT_ONE_TEXT).text
        return text_before, text_after

    @allure.step('check_old_stile_menu')
    def check_old_stile_menu(self):
        select = Select(self.element_is_visible(self.locators.OLD_STYLE_INPUT_LIST))
        text_before = self.element_is_visible(self.locators.OLD_STYLE_TEXT).text
        index = random.randint(1, 10)
        select.select_by_index(index)
        text_after = self.driver.find_element(By.CSS_SELECTOR,
                                              f'select[id="oldSelectMenu"] option[value="{index}"]').text
        return text_before, text_after

    @allure.step('check_multy_dropdown')
    def check_multy_dropdown(self):
        input_field = self.element_is_present(self.locators.MULTISELECT_INPUT)
        self.element_is_visible(self.locators.MULTISELECT_FIELD).click()
        # input_field.click()
        input_field.send_keys('g')
        input_field.send_keys(Keys.RETURN)
        dropdown_list = self.elements_are_present(self.locators.MULTISELECT_INPUT_LIST)
        for _ in dropdown_list:
            input_field.send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.MULTISELECT_ITEMS_CROSS).click()

        time.sleep(0.5)
        self.element_is_visible(self.locators.MULTISELECT_FIELD).click()
        dropdown_list = self.elements_are_visible(self.locators.MULTISELECT_INPUT_LIST)
        for _ in dropdown_list:
            input_field.send_keys(Keys.RETURN)
        item_cross_before = self.elements_are_visible(self.locators.MULTISELECT_ITEM_CROSS)
        item_cross_before[random.randint(0, len(item_cross_before) - 1)].click()
        time.sleep(0.2)
        item_cross_after = self.elements_are_visible(self.locators.MULTISELECT_ITEM_CROSS)
        return len(item_cross_before) - len(item_cross_after)

    @allure.step('check_standard_multiselect')
    def check_standard_multiselect(self):
        select = Select(self.element_is_visible(self.locators.STANDARD_MULTISELECT_INPUT))
        num_index = len(self.elements_are_present(self.locators.STANDARD_MULTISELECT_INPUT_LIST))
        try:
            index = random.randint(0, num_index - 1)
            select.select_by_index(index)
            index = random.randint(0, num_index - 1)
            select.select_by_index(index)
            return True
        except NoSuchElementException:
            return False

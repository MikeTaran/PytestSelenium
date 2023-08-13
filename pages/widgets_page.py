import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from locators.widgets_page_locators import AccordianWidgetsPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage


class AccordianWidgetsPage(BasePage):
    locators = AccordianWidgetsPageLocators()

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
            content = len(content_list[i].text)
            if content == 0:
                title_list[i].click()
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

    def check_single_input(self, letter):
        single_input = self.element_is_visible(self.locators.SINGLE_INPUT)
        single_input.send_keys(letter)
        single_input.send_keys(Keys.RETURN)
        result = self.element_is_visible(self.locators.SINGLE_INPUT_RESULT).text
        return result

    def check_multy_element_deletion(self):
        result = self.check_multy_input(['a', 'b', 'q', 'w'])
        index = random.randint(0, 3)
        delete_cross = self.elements_are_visible(self.locators.REMOVE_MULTY_ELEMENT)
        delete_cross[index].click()
        result_list = self.elements_are_visible(self.locators.MULTY_INPUT_RESULT_LIST)
        return len(result), len(result_list)

    def test_all_multy_deletion(self):

        self.check_multy_input(['a', 'b', 'q', 'w'])
        all_delete_cross = self.element_is_visible(self.locators.REMOVE_ALL_MULTY_ELEMENT)
        all_delete_cross.click()
        try:
            self.element_is_not_visible(self.locators.MULTY_INPUT_RESULT_LIST)
            return True
        except TimeoutException:
            return False

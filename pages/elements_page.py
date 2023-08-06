import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.element_page_locators import TextBoxPageLocators, CheckBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        submit_btn = self.find_element(self.locators.SUBMIT)
        self.go_to_element(submit_btn)
        submit_btn.click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        curr_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        perm_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, curr_address, perm_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def expand_checkbox_lict(self):
        self.element_is_visible(self.locators.BTN_EXPAND_ALL).click()

    def collapse_checkbox_list(self):
        self.element_is_visible(self.locators.BTN_COLLAPSE_ALL).click()

    def click_random_checkbox(self):
        checkbox_list = self.elements_are_present(self.locators.CHECKBOX_ITEM_LIST)
        print('\n', len(checkbox_list))
        for _ in range(len(checkbox_list)):
            item = checkbox_list[random.randint(0, len(checkbox_list) - 1)]
            self.go_to_element(item)
            item.click()

    def get_checked_list(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_LIST)
        print(len(checked_list))
        checked_title_list = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            checked_title_list.append(title_item.text)
        print(checked_title_list)
        return str(checked_title_list).replace(' ', '').replace('.doc', '').lower()

    def get_output_result(self):
        output_list = self.elements_are_present(self.locators.OUTPUT_LIST)
        print(len(output_list))
        checked_output_list = []
        for item in output_list:
            checked_output_list.append(item.text)
        print(checked_output_list)
        return str(checked_output_list).replace(' ', '').lower()

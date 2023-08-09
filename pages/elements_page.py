import base64
import os
import random
import time

import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from locators.element_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, DownUploadPageLocators, DynamicPropsPageLocators
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
        for _ in range(len(checkbox_list)):
            item = checkbox_list[random.randint(0, len(checkbox_list) - 1)]
            self.go_to_element(item)
            item.click()

    def get_checked_list(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_LIST)
        checked_title_list = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            checked_title_list.append(title_item.text)
        return str(checked_title_list).replace(' ', '').replace('.doc', '').lower()

    def get_output_result(self):
        output_list = self.elements_are_present(self.locators.OUTPUT_LIST)
        checked_output_list = []
        for item in output_list:
            checked_output_list.append(item.text)
        return str(checked_output_list).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_radio_button(self, choice):
        choices = {
            'yes': self.locators.radio_btn_yes,
            'impressive': self.locators.radio_btn_impress,
            'no': self.locators.radio_btn_no
        }
        radio = self.element_is_visible(choices[choice])
        radio.click()

    def get_output_result(self):
        return self.element_is_present(self.locators.output_message).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self, count=1):
        data_input = []
        # count = random.randint(1, 3)
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            #
            data_input.append([firstname, lastname, str(age), email, str(salary), department])
            count -= 1
        return data_input

    def get_full_persons_list(self):
        data_output = []
        persons_list = self.elements_are_present(self.locators.FULL_PERSONS_LIST)
        for row_list in persons_list:
            # разделение текста по разделителю переноса строки '\n' : list.splitlines()
            data_output.append(row_list.text.splitlines())
        return data_output

    def get_empty_row_qty(self):
        return len(self.elements_are_present(self.locators.EMPTY_ROW_LIST))

    def search_person(self, key_word):
        search_field = self.element_is_visible(self.locators.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(key_word)

    def get_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def get_delete_confirmation(self):
        return self.element_is_present(self.locators.DELETE_CONFIRMATION).text

    def change_rows_count(self):
        count = [5, 10, 20, 25]
        data = []
        count_row_button = self.element_is_visible(self.locators.COUNT_ROWS)
        for x in count:
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.get_count_rows())
        return data, count

    def change_rows_count_fail(self):
        count = [50, 100]
        data = []
        count_row_button = self.element_is_visible(self.locators.COUNT_ROWS)
        for x in count:
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_present((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.get_count_rows())
        return data, count

    def get_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PERSONS_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        if type_click == 'double':
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
            return self.get_success_message(self.locators.DOUBLE_CLICK_MESSAGE)

        if type_click == 'right':
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.get_success_message(self.locators.RIGHT_CLICK_MESSAGE)

        if type_click == 'click':
            self.element_is_visible(self.locators.DYNAMIC_CLICK_BUTTON).click()
            return self.get_success_message(self.locators.DYNAMIC_CLICK_MESSAGE)

    def get_success_message(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_link(self, type_link):
        new_tab_link = ''
        if type_link == 'simple':
            new_tab_link = self.element_is_visible(self.locators.SIMPLE_HOME_LINK)
        elif type_link == 'dynamic':
            new_tab_link = self.element_is_visible(self.locators.DYNAMIC_HOME_LINK)
        href = new_tab_link.get_attribute('href')
        request = requests.get(href).status_code
        if request == 200:
            new_tab_link.click()
            tab_list = self.driver.window_handles
            self.driver.switch_to.window(tab_list[1])
            tab_url = self.driver.current_url
            self.driver.switch_to.window(tab_list[0])
            return href, tab_url
        else:
            return href, request

    def check_api_link(self, i):
        api_links = {
            'Created': 'https://demoqa.com/created',
            'No Content': 'https://demoqa.com/no-content',
            'Moved': 'https://demoqa.com/moved',
            'Bad Request': 'https://demoqa.com/bad-request',
            'Unauthorized': 'https://demoqa.com/unauthorized',
            'Forbidden': 'https://demoqa.com/forbidden',
            'Not Found': 'https://demoqa.com/invalid-url',
        }

        links_list = self.elements_are_present(self.locators.LIST_API_LINKS)
        name_link = links_list[i].text
        request = requests.get(api_links[name_link]).status_code
        links_list[i].click()
        time.sleep(2)
        response_message = self.elements_are_present(self.locators.SUCCESS_MESSAGE)
        code = response_message[0].text
        status = response_message[1].text
        return name_link, request, code, status


class DownUploadPage(BasePage):
    locators = DownUploadPageLocators()

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_BUTTON).send_keys(path)
        os.remove(path)
        uploaded_message = self.element_is_present(self.locators.UPLOADED_MESSAGE).text
        name = file_name.split('\\')[-1]
        message = uploaded_message.split('\\')[-1]
        return name, message

    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_BUTTON).get_attribute('href').split(',')
        link_b64 = base64.b64decode(link[1])
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        file_path = os.path.join(current_dir, f'filetest_{random.randint(1, 999)}.jpg')
        with open(file_path, "wb+") as my_file:
            my_file.write(link_b64)
            check_file = os.path.exists(file_path)
            my_file.close()
        os.remove(file_path)
        return check_file


class DynamicPropsPage(BasePage):
    locators = DynamicPropsPageLocators()

    def get_text_id(self):
        text = self.element_is_visible(self.locators.DYNAMIC_TEXT)
        text_id_1 = text.get_attribute('id')
        self.refresh_window()
        text = self.element_is_visible(self.locators.DYNAMIC_TEXT)
        text_id_2 = text.get_attribute('id')
        return text_id_1, text_id_2


    def enable_button(self):
        try:
            return self.element_is_clickable(self.locators.ENABLE_ALERT_BUTTON)
        except TimeoutException:
            return False

    def color_change(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    def visible_button(self):
        try:
            return self.element_is_visible(self.locators.VISIBLE_ALERT_BUTTON)
        except TimeoutException:
            return False

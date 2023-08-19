import base64
import os
import random
import time

import allure
import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from locators.element_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, DownUploadPageLocators, DynamicPropsPageLocators, \
    BrokenLinksPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step('fill_all_fields')
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

    @allure.step('check_filled_form')
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        curr_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        perm_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, curr_address, perm_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step('expand_checkbox_lict')
    def expand_checkbox_lict(self):
        self.element_is_visible(self.locators.BTN_EXPAND_ALL).click()

    @allure.step('collapse_checkbox_list')
    def collapse_checkbox_list(self):
        self.element_is_visible(self.locators.BTN_COLLAPSE_ALL).click()

    @allure.step('click_random_checkbox')
    def click_random_checkbox(self):
        checkbox_list = self.elements_are_present(self.locators.CHECKBOX_ITEM_LIST)
        for _ in range(len(checkbox_list)):
            item = checkbox_list[random.randint(0, len(checkbox_list) - 1)]
            self.go_to_element(item)
            item.click()

    @allure.step('get_checked_list')
    def get_checked_list(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_LIST)
        checked_title_list = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            checked_title_list.append(title_item.text)
        return str(checked_title_list).replace(' ', '').replace('.doc', '').lower()

    @allure.step('get_output_result')
    def get_output_result(self):
        output_list = self.elements_are_present(self.locators.OUTPUT_LIST)
        checked_output_list = []
        for item in output_list:
            checked_output_list.append(item.text)
        return str(checked_output_list).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step('click_radio_button')
    def click_radio_button(self, choice):
        choices = {
            'yes': self.locators.radio_btn_yes,
            'impressive': self.locators.radio_btn_impress,
            'no': self.locators.radio_btn_no
        }
        radio = self.element_is_visible(choices[choice])
        radio.click()

    @allure.step('get_output_result')
    def get_output_result(self):
        return self.element_is_present(self.locators.output_message).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.step('add_new_person')
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

    @allure.step('get_full_persons_list')
    def get_full_persons_list(self):
        data_output = []
        persons_list = self.elements_are_present(self.locators.FULL_PERSONS_LIST)
        for row_list in persons_list:
            # разделение текста по разделителю переноса строки '\n' : list.splitlines()
            data_output.append(row_list.text.splitlines())
        return data_output

    @allure.step('get_empty_row_qty')
    def get_empty_row_qty(self):
        return len(self.elements_are_present(self.locators.EMPTY_ROW_LIST))

    @allure.step('search_person')
    def search_person(self, key_word):
        search_field = self.element_is_visible(self.locators.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(key_word)

    @allure.step('get_search_person')
    def get_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('update_person_info')
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    @allure.step('delete_person')
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('get_delete_confirmation')
    def get_delete_confirmation(self):
        return self.element_is_present(self.locators.DELETE_CONFIRMATION).text

    @allure.step('change_rows_count')
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

    @allure.step('change_rows_count_fail')
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

    @allure.step('get_count_rows')
    def get_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PERSONS_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step('click_on_different_button')
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

    @allure.step('get_success_message')
    def get_success_message(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step('check_new_tab_link')
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

    @allure.step('check_api_link')
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

    @allure.step('upload_file')
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_BUTTON).send_keys(path)
        os.remove(path)
        uploaded_message = self.element_is_present(self.locators.UPLOADED_MESSAGE).text
        name = file_name.split('\\')[-1]
        message = uploaded_message.split('\\')[-1]
        return name, message

    @allure.step('download_file')
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

    @allure.step('get_text_id')
    def get_text_id(self):
        text = self.element_is_visible(self.locators.DYNAMIC_TEXT)
        text_id_1 = text.get_attribute('id')
        self.refresh_window()
        text = self.element_is_visible(self.locators.DYNAMIC_TEXT)
        text_id_2 = text.get_attribute('id')
        return text_id_1, text_id_2

    @allure.step('enable_button')
    def enable_button(self):
        try:
            return self.element_is_clickable(self.locators.ENABLE_ALERT_BUTTON)
        except TimeoutException:
            return False

    @allure.step('color_change')
    def color_change(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    @allure.step('visible_button')
    def visible_button(self):
        try:
            return self.element_is_visible(self.locators.VISIBLE_ALERT_BUTTON)
        except TimeoutException:
            return False


class BrokenLinksPage(BasePage):
    locators = BrokenLinksPageLocators()

    @allure.step('check_link')
    def check_link(self):
        links = self.find_elements(self.locators.LINK_LIST)
        for link in links:
            href = link.get_attribute('href')
            if not href:
                continue
            response = requests.head(href)
            assert response.status_code < 400, f"Broken link: {href}, {response}"

    @allure.step('check_image')
    def check_image(self):
        images = self.find_elements(self.locators.IMAGES_LIST)
        for img in images:
            src = img.get_attribute("src")
            if not src:
                print(f'The img{img} has No src attribute')
                continue
            natural_width = self.driver.execute_script("return arguments[0].naturalWidth;", img)
            assert natural_width != 0, f"Broken image: {src}"

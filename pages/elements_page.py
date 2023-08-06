import random


from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.element_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators
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
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def get_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()



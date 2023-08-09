import base64
import os
import random
import time

import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from locators.forms_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormsPage(BasePage):
    locators = FormPageLocators()

    def fill_static_fields(self):
        person_info = next(generated_person())
        first_name = person_info.firstname
        last_name = person_info.lastname
        full_name = f'{first_name} {last_name}'
        email = person_info.email
        mobile = person_info.phone_10
        current_address = person_info.current_address

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.MOBILE).send_keys(mobile)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        submit_btn = self.find_element(self.locators.SUBMIT_BUTTON)
        return full_name, email, mobile, current_address

    def fill_gender_radiobutton(self):
        gender_list = self.elements_are_present(self.locators.GENDER_LIST)
        rnd_i = random.randint(0, 2)
        gender_list[rnd_i].click()
        radiobutton_name = gender_list[rnd_i].text
        return radiobutton_name

    def fill_date_of_birth(self):
        person_info = next(generated_person())
        birthday = person_info.birthday
        date_of_birth = self.element_is_visible(self.locators.DATE_OF_BIRTH)
        date_of_birth.clear()
        date_of_birth.send_keys(birthday)
        self.element_is_visible(self.locators.SUBJECT).click()

    def fill_hobbies_checkboxes(self):
        hobbies_list = self.elements_are_visible(self.locators.HOBBIES_LIST)
        for _ in range(10):
            hobbies_list[random.randint(0, 2)].click()

    def get_checked_hobbies_list(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_LIST)
        checked_title_list = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            checked_title_list.append(title_item.text)
        return str(checked_title_list).replace(' ', '').replace('.doc', '').lower()

    def upload_picture(self):
        file_name, path = generated_file('jpg')
        self.element_is_present(self.locators.UPLOAD_FILE_BUTTON).send_keys(path)
        os.remove(path)
        # uploaded_message = self.element_is_present(self.locators.UPLOADED_MESSAGE).text
        name = file_name.split('\\')[-1]
        # message = uploaded_message.split('\\')[-1]
        return name

    def fill_subject_field(self):
        self.element_is_visible(self.locators.SUBJECT).send_keys('English')

    def fill_state_and_city_fields(self):
        pass

    def submit_input(self):
        self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()

    def check_submitted_form_present(self):
        try:
            self.element_is_visible(self.locators.SUBMITTED_FORM)
            return True
        except:
            return False

    def get_submitted_data(self):
        data = []
        data_list = self.elements_are_present(self.locators.SUBMITTED_FORM_DATA)
        for item in data_list:
            data.append(item.text)
        return data

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
import os
import random
import pyautogui

from selenium.common import TimeoutException
from selenium.webdriver import Keys

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
        return full_name, email, mobile, current_address

    def fill_gender_radiobutton(self):
        gender_list = self.elements_are_present(self.locators.GENDER_LIST)
        rnd_i = random.randint(0, 2)
        gender_list[rnd_i].click()
        radiobutton_name = gender_list[rnd_i].text
        return radiobutton_name

    def fill_date_of_birth(self):
        person_info = next(generated_person())
        core_tab = self.driver.window_handles[0]
        birthday = person_info.birthday
        date_of_birth_input = self.element_is_visible(self.locators.DATE_OF_BIRTH)
        date_of_birth_input.click()
        self.driver.execute_script("window.navigator.clipboard.writeText(arguments[0])", birthday)
        date_of_birth_input.send_keys(Keys.CONTROL, 'a')
        date_of_birth_input.send_keys(Keys.CONTROL, 'v')
        # не работает в headless режиме - не видит локатор
        self.driver.switch_to.window(core_tab)
        date_of_birth_input = self.element_is_visible(self.locators.DATE_OF_BIRTH)
        date_of_birth_input.send_keys(Keys.RETURN)
        return birthday

    def fill_hobbies_checkboxes(self):
        hobbies_txt = ['Sports', 'Reading', 'Music']
        hobbies_list = self.elements_are_visible(self.locators.HOBBIES_LIST)
        rnd_i = random.randint(1, 2)
        hobbies_list[0].click()
        hobbies_list[rnd_i].click()
        return f'{hobbies_txt[0]}, {hobbies_txt[rnd_i]}'

    def get_checked_hobbies_list(self):
        pass

    def upload_picture(self):
        file_name, path = generated_file('jpg')
        self.element_is_present(self.locators.UPLOAD_FILE_BUTTON).send_keys(path)
        os.remove(path)
        # uploaded_message = self.element_is_present(self.locators.UPLOADED_MESSAGE).text
        name = file_name.split('\\')[-1]
        # message = uploaded_message.split('\\')[-1]
        return name

    def fill_subject_field(self):
        input_field = (self.element_is_visible(self.locators.SUBJECT))
        sub = ["English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
               "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
        subject = sub[random.randint(0, len(sub) - 1)]
        input_field.send_keys(subject)
        input_field.send_keys(Keys.RETURN)
        return subject

    def fill_state_and_city_fields(self):
        state = 'NCR'
        city = 'Noida'
        self.element_is_visible(self.locators.STATE_SELECT).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(state)
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.CITY_SELECT).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(city)
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        return f'{state} {city}'

    def check_submit_button(self):
        self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()

    def check_close_button(self):
        self.element_is_clickable(self.locators.CLOSE_BUTTON).click()

    def check_submitted_form_present(self):
        try:
            self.element_is_visible(self.locators.SUBMITTED_FORM)
            return True
        except TimeoutException:
            return False

    def check_submitted_form_not_present(self):
        try:
            self.element_is_not_visible(self.locators.SUBMITTED_FORM)
            return True
        except TimeoutException:
            return False

    def get_submitted_data(self):
        data = []
        data_list = self.elements_are_present(self.locators.SUBMITTED_FORM_DATA)
        for item in data_list:
            data.append(item.text)
        return data

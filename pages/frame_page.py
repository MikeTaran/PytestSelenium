from generator.generator import generated_person
from locators.frame_page_locators import WindowsTabPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class WindowsTabPage(BasePage):
    locators = WindowsTabPageLocators()

    def windows_new_tab(self, method):
        available_cases = {
            'tab': self.locators.NEW_TAB_BUTTON,
            'window': self.locators.NEW_WINDOW_BUTTON
        }
        self.element_is_visible(available_cases[method]).click()
        number_of_tabs = len(self.driver.window_handles)
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
        new_tab = self.element_is_visible(self.locators.NEW_TAB_TEXT)
        text_id = new_tab.get_attribute('id')
        new_tab_text = new_tab.text
        new_tab_url = self.driver.current_url
        self.driver.close()
        core_tab = self.driver.window_handles[0]
        self.driver.switch_to.window(core_tab)
        self.element_is_visible(self.locators.NEW_TAB_BUTTON)
        core_tab_url = self.driver.current_url
        return new_tab_text, text_id, core_tab_url, new_tab_url, number_of_tabs


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def simple_alert(self):
        self.element_is_visible(self.locators.SIMPLE_ALERT_BUTTON).click()
        self.alert_is_present()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        print(alert_text)

    def time_alert(self):
        self.element_is_visible(self.locators.TIME_ALERT_BUTTON).click()
        self.alert_is_present(10)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        print(alert_text)

    def confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        self.alert_is_present()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        confirm_text = self.element_is_visible(self.locators.CONFIRM_ALERT_RESULT).text
        print(alert_text, confirm_text)
        #
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        self.alert_is_present()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.dismiss()
        confirm_text = self.element_is_visible(self.locators.CONFIRM_ALERT_RESULT).text
        print(alert_text, confirm_text)

    def prompt_alert(self):
        person_info = next(generated_person())
        first_name = person_info.firstname
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        self.alert_is_present()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.send_keys(first_name)
        alert.accept()
        confirm_text = self.element_is_visible(self.locators.PROMPT_ALERT_RESULT).text
        print(alert_text, confirm_text, first_name)

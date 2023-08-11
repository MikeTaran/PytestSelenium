from generator.generator import generated_person
from locators.frame_page_locators import WindowsTabPageLocators, AlertsPageLocators, IframesPageLocators
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
        return alert_text

    def time_alert(self):
        self.element_is_visible(self.locators.TIME_ALERT_BUTTON).click()
        self.alert_is_present(10)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        self.alert_is_present()
        alert = self.driver.switch_to.alert
        alert.accept()
        confirm_text = self.element_is_visible(self.locators.CONFIRM_ALERT_RESULT).text
        #
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        self.alert_is_present()
        alert = self.driver.switch_to.alert
        alert.dismiss()
        dismiss_text = self.element_is_visible(self.locators.CONFIRM_ALERT_RESULT).text
        return confirm_text, dismiss_text

    def prompt_alert(self):
        person_info = next(generated_person())
        first_name = person_info.firstname
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        self.alert_is_present()
        alert = self.driver.switch_to.alert
        alert.send_keys(first_name)
        alert.accept()
        confirm_text = self.element_is_visible(self.locators.PROMPT_ALERT_RESULT).text
        return confirm_text, first_name


class IframesPage(BasePage):
    locators = IframesPageLocators()

    def check_iframe(self, num_frame):
        locator = ''
        if num_frame == 'frame1':
            locator = self.locators.IFRAME_1
        if num_frame == 'frame2':
            locator = self.locators.IFRAME_2
        iframe = self.element_is_visible(locator)
        width = iframe.get_attribute('width')
        height = iframe.get_attribute('height')
        self.driver.switch_to.frame(iframe)
        iframe_text = self.element_is_visible(self.locators.IFRAME_TEXT).text
        self.driver.switch_to.default_content()
        return [width, height, iframe_text]

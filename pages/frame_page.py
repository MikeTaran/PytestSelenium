import time

from locators.frame_page_locators import WindowsTabPageLocators
from pages.base_page import BasePage


class WindowsTabPage(BasePage):
    locators = WindowsTabPageLocators()

    def windows_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
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
        return new_tab_text, text_id, core_tab_url, new_tab_url

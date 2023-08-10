from selenium.webdriver.common.by import By


class WindowsTabPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_TAB_TEXT = (By.CSS_SELECTOR, 'h1')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    NEW_WINDOW_MESSAGE_BUTTON = (By.CSS_SELECTOR, 'button[id="msgWindowButtonWrapper"]')

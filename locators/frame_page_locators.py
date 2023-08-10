from selenium.webdriver.common.by import By


class WindowsTabPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_TAB_TEXT = (By.CSS_SELECTOR, 'h1')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    NEW_WINDOW_MESSAGE_BUTTON = (By.CSS_SELECTOR, 'button[id="msgWindowButtonWrapper"]')


class AlertsPageLocators:
    SIMPLE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    TIME_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CONFIRM_ALERT_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_ALERT_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')
    PROMPT_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')

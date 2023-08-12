from selenium.webdriver.common.by import By


class AccordianWidgetsPageLocators:
    ACCORDIAN_LIST = (By.CSS_SELECTOR, 'div[class="card"]')
    ACCORDIAN_TITLE_LIST = (By.CSS_SELECTOR, 'div[class="card-header"]')
    ACCORDIAN_CONTENT_LIST = (By.CSS_SELECTOR, 'div[id*="Content"]')

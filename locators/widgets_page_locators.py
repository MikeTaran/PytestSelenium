from selenium.webdriver.common.by import By


class AccordianWidgetsPageLocators:
    ACCORDIAN_LIST = (By.CSS_SELECTOR, 'div[class="card"]')
    ACCORDIAN_TITLE_LIST = (By.CSS_SELECTOR, 'div[class="card-header"]')
    ACCORDIAN_CONTENT_LIST = (By.CSS_SELECTOR, 'div[id*="Content"]')


class AutoCompletePageLocators:
    MULTY_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id = "autoCompleteSingleInput"]')
    SINGLE_INPUT_RESULT = (By.CSS_SELECTOR, 'div[class^="auto-complete__single-value"]')
    MULTY_INPUT_RESULT_LIST = (By.CSS_SELECTOR, 'div[class*="auto-complete__multi-value__label"]')
    REMOVE_MULTY_ELEMENT = (By.CSS_SELECTOR, 'div[class="css-xb97g8 auto-complete__multi-value__remove"]')
    REMOVE_ALL_MULTY_ELEMENT = (By.CSS_SELECTOR, 'div.auto-complete__clear-indicator')


 
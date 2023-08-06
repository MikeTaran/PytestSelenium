from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # reg form fields
    FULL_NAME = (By.CSS_SELECTOR, "input#userName")
    EMAIL = (By.CSS_SELECTOR, "input#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea#permanentAddress")
    SUBMIT = (By.CSS_SELECTOR, "button#submit")

    # created form fields
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    BTN_EXPAND_ALL = (By.CSS_SELECTOR, "button[title='Expand all']")
    BTN_COLLAPSE_ALL = (By.CSS_SELECTOR, "button[title='Collapse all']")
    CHECKBOX_ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_LIST = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_LIST = (By.CSS_SELECTOR, "#result .text-success")



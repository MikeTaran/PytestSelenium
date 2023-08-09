from selenium.webdriver.common.by import By


class FormPageLocators:
    # reg form fields
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    GENDER_LIST = (By.CSS_SELECTOR, 'input[name = "gender"]')
    MOBILE = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    SUBJECT = (By.CSS_SELECTOR, 'div[id="subjectsContainer"]')
    HOBBIES_LIST = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    UPLOAD_FILE_BUTTON = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    # created form fields
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

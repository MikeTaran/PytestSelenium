from selenium.webdriver.common.by import By


class FormPageLocators:
    # reg form fields
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    GENDER_LIST = (By.CSS_SELECTOR, 'div[class*="custom-radio"] label')
    MOBILE = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    SUBJECT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    HOBBIES_LIST = (By.CSS_SELECTOR, 'div[class*="custom-checkbox"] label')
    UPLOAD_FILE_BUTTON = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    STATE_SELECT = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    CITY_SELECT = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    # created form fields
    SUBMITTED_FORM = (By.CSS_SELECTOR, 'div[class="modal-content"]')
    SUBMITTED_FORM_DATA = (By.CSS_SELECTOR, 'tbody tr td:nth-child(2)')
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')

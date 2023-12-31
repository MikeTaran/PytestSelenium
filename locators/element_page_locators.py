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


class RadioButtonPageLocators:
    list_radio_btn = (By.CSS_SELECTOR, "div input")
    radio_btn_yes = (By.CSS_SELECTOR, "label[for='yesRadio']")
    radio_btn_impress = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    radio_btn_no = (By.CSS_SELECTOR, "label[for='noRadio']")
    output_message = (By.CSS_SELECTOR, "p [class = 'text-success']")


class WebTablePageLocators:
    # add new person form
    ADD_BUTTON = (By.CSS_SELECTOR, "#addNewRecordButton")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "div[class='modal-content']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    FULL_PERSONS_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    EMPTY_ROW_LIST = (By.CSS_SELECTOR, 'div .-padRow')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    EDIT_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
    COUNT_ROWS = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
    # delete person
    DELETE_CONFIRMATION = (By.CSS_SELECTOR, 'div [class="rt-noData"]')


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    DYNAMIC_CLICK_BUTTON = (By.XPATH, '//div[3]/button')
    # result
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    DYNAMIC_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinksPageLocators:
    # id="bad-request"
    SIMPLE_HOME_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    DYNAMIC_HOME_LINK = (By.CSS_SELECTOR, 'a[id="dynamicLink"]')
    LIST_API_LINKS = (By.CSS_SELECTOR, 'p>a')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'p[id="linkResponse"] b')


class DownUploadPageLocators:
    UPLOAD_BUTTON = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_MESSAGE = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, 'a[id="downloadButton"]')


class DynamicPropsPageLocators:
    DYNAMIC_TEXT = (By.XPATH, "//*[contains(text(), 'random Id')]")
    ENABLE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    VISIBLE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')


class BrokenLinksPageLocators:
    VALID_IMAGE = (By.CSS_SELECTOR, 'img[src="/images/Toolsqa.jpg"]')
    BROKEN_IMAGE = (By.CSS_SELECTOR, 'img[src="/images/Toolsqa_1.jpg"]')
    VALID_LINK = (By.CSS_SELECTOR, 'a[href="http://demoqa.com"]')
    BROKEN_LINK = (By.CSS_SELECTOR, 'a[href="http://the-internet.herokuapp.com/status_codes/500"]')
    IMAGES_LIST = (By.CSS_SELECTOR, 'div[class="col-12 mt-4 col-md-6"] img')
    LINK_LIST = (By.CSS_SELECTOR, 'div[class="col-12 mt-4 col-md-6"] a')

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


class DatePickerPageLocators:
    ONLY_DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    ONLY_DATE_DAY_INPUT_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__day')
    ONLY_DATE_MONTH_INPUT_SELECT = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    ONLY_DATE_YEAR_INPUT_SELECT = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')

    DATE_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_TIME_MONTH_INPUT = (By.CSS_SELECTOR, 'span.react-datepicker__month-read-view--down-arrow')
    DATE_TIME_MONTH_INPUT_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__month-option')
    DATE_TIME_YEAR_INPUT = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_TIME_YEAR_INPUT_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__year-option')
    DATE_TIME_TIME_INPUT_LIST = (By.CSS_SELECTOR, 'ul[class="react-datepicker__time-list"] li')
    DATE_TIME_DAY_INPUT_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__day')
    DATE_TIME_YEAR_NAVIGATION_ARROW = (By.CSS_SELECTOR, 'a.react-datepicker__navigation')


class SliderPageLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')

    PROGRESSIVE_BAR_START_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRESSIVE_BAR_RESET_BUTTON = (By.CSS_SELECTOR, 'button[id="resetButton"]')
    PROGRESSIVE_BAR_VALUE = (By.CSS_SELECTOR, 'div[role="progressbar"]')


class TabsPageLocators:
    TABS_LIST = (By.CSS_SELECTOR, 'nav[role="tablist"] a')
    TAB_CONTENT = (By.CSS_SELECTOR, 'div[class="tab-content"]')


class ToolTipsPageLocators:
    HOVER_BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    INPUT_FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    TEXT_TOOLTIPS_LIST = (By.CSS_SELECTOR, 'div[id="texToolTopContainer"]>a')


class MenuPageLocators:
    MAIN_ITEM_1 = (By.CSS_SELECTOR, '')
    MAIN_ITEM_2 = (By.CSS_SELECTOR, '')
    MAIN_ITEM_3 = (By.CSS_SELECTOR, '')


class SelectMenuPageLocators:
    VALUE_INPUT = (By.CSS_SELECTOR, '')
    SELECT_INPUT = (By.CSS_SELECTOR, '')
    OLD_STYLE_INPUT = (By.CSS_SELECTOR, '')
    MULTISELECT_INPUT = (By.CSS_SELECTOR, '')
    STANDARD_MULTISELECT_INPUT = (By.CSS_SELECTOR, '')

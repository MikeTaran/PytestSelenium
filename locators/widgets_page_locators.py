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
    BUTTON_TOOLTIP = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    INPUT_FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    INPUT_FIELD_TOOLTIP = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    CONTRARY_TEXT = (By.CSS_SELECTOR, 'div[id="texToolTopContainer"]>a:first-child')
    CONTRARY_TEXT_TOOLTIP = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"')

    NUMBER_TEXT = (By.CSS_SELECTOR, 'div[id="texToolTopContainer"]>a:last-child')
    NUMBER_TEXT_TOOLTIP = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"')

    HOVER_TOOLTIP = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')


class MenuPageLocators:
    MAIN_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')


class SelectMenuPageLocators:
    SELECT_VALUE = (By.CSS_SELECTOR, 'div[id="withOptGroup"]')
    SELECT_VALUE_TEXT = (By.CSS_SELECTOR, 'div[id="withOptGroup"] div[class*="singleValue"]')
    SELECT_VALUE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-2-input"]')
    SELECT_VALUE_INPUT_LIST = (By.CSS_SELECTOR, 'div[id*="react-select-2-option"]')

    SELECT_ONE = (By.CSS_SELECTOR, 'div[id="selectOne"]')
    SELECT_ONE_TEXT = (By.CSS_SELECTOR, 'div[id="selectOne"] div[class*="singleValue"]')
    SELECT_ONE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_ONE_INPUT_LIST = (By.CSS_SELECTOR, 'div[id*="react-select-3-option"]')

    OLD_STYLE_INPUT_LIST = (By.CSS_SELECTOR, 'select[id="oldSelectMenu"]')
    OLD_STYLE_TEXT = (By.CSS_SELECTOR, 'select[id="oldSelectMenu"] option')

    MULTISELECT_FIELD = (By.XPATH, "(//div[contains(@class,'css-1hwfws3')])[3]")
    MULTISELECT_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    MULTISELECT_INPUT_LIST = (By.CSS_SELECTOR, 'div[id*="react-select-4-option"]')

    MULTISELECT_LIST = (By.CSS_SELECTOR, 'div[class*="multiValue"]')
    MULTISELECT_ITEM_CROSS = (By.CSS_SELECTOR, 'div[class*="multiValue"] svg')
    MULTISELECT_ITEMS_CROSS = (By.XPATH, "(//*[name()='svg'][@class='css-19bqh2r'])[7]")

    STANDARD_MULTISELECT_INPUT = (By.CSS_SELECTOR, 'select[id="cars"]')

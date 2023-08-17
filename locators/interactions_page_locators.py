from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_TAB_LIST = (By.CSS_SELECTOR, 'div[class*="vertical-list-container"]>div')

    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid""]')
    GRID_TAB_LIST = (By.CSS_SELECTOR, 'div[class="create-grid"]>div')


class SelectablePage:
    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_TAB_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"]>ul>li')

    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid""]')
    GRID_TAB_LIST = (By.CSS_SELECTOR, 'div[id="gridContainer"] li')

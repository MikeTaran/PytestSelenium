from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_TAB_LIST = (By.CSS_SELECTOR, 'div[class*="vertical-list-container"]>div')

    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_TAB_LIST = (By.CSS_SELECTOR, 'div[class="create-grid"]>div')


class SelectablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_TAB_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"]>ul>li')
    LIST_TAB_LIST_ACTIVE = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"]>ul>li[class*="active"]')

    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_TAB_LIST = (By.CSS_SELECTOR, 'div[id="gridContainer"] li')
    GRID_TAB_LIST_ACTIVE = (By.CSS_SELECTOR, 'div[id="gridContainer"] li[class*="active"]')


class ResizablePagelocators:
    BOX_1 = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    BOX_1_ANCHOR = (By.CSS_SELECTOR, '')
    BOX_2 = (By.CSS_SELECTOR, 'div[id="resizable"]')
    BOX_2_ANCHOR = (By.CSS_SELECTOR, '')

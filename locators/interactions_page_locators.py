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


class ResizablePageLocators:
    BOX_1 = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    BOX_1_ANCHOR = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"] span')
    BOX_2 = (By.CSS_SELECTOR, 'div[id="resizable"]')
    BOX_2_ANCHOR = (By.CSS_SELECTOR, 'div[id="resizable"] span')


class DroppablePageLocators:
    # SIMPLE
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    DRAG = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROP_SIMPLE = (By.CSS_SELECTOR, 'div[id="droppableExample-tabpane-simple"] div[id="droppable"]')
    DROP_SIMPLE_TITLE = (By.CSS_SELECTOR, 'div[id="droppableExample-tabpane-simple"] div[id="droppable"] p')
    # ACCEPT
    ACCEPT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    DRAG_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    DRAG_NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    DROP_ACCEPT = (By.CSS_SELECTOR, 'div[id="acceptDropContainer"] div[id="droppable"]')
    DROP_ACCEPT_TITLE = (By.CSS_SELECTOR, 'div[id="acceptDropContainer"] div[id="droppable"] p')
    # PREVENT
    PREVENT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    DRAG_PREVENT = (By.CSS_SELECTOR, 'div[id="dragBox"]')
    OUTER_NOT_GREEDY = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"]')
    OUTER_NOT_GREEDY_TITLE = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p')
    INNER_NOT_GREEDY = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    INNER_NOT_GREEDY_TITLE = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"] p')
    OUTER_GREEDY = (By.CSS_SELECTOR, 'div[id="greedyDropBox"]')
    OUTER_GREEDY_TITLE = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p')
    INNER_GREEDY = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')
    INNER_GREEDY_TITLE = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"] p')
    # REVERT
    REVERT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    DRAG_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    DRAG_NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_REVERT = (By.CSS_SELECTOR, 'div[id="revertableDropContainer"] div[id="droppable"]')
    DROP_REVERT_TITLE = (By.CSS_SELECTOR, 'div[id="revertableDropContainer"] div[id="droppable"] p')


class DraggablePageLocators:
    # SIMPLE
    TAB_SIMPLE = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    DRAG_SIMPLE = (By.CSS_SELECTOR, 'div[id="dragBox"]')
    # AXIS
    TAB_AXIS = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    DRAG_X = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    DRAG_Y = (By.CSS_SELECTOR, 'div[id="restrictedY"]')
    # CONTAINER
    TAB_CONTAINER = (By.CSS_SELECTOR, '')
    DRAG_CONTAINED = (By.CSS_SELECTOR, '')
    # CURSOR
    TAB_CURSOR = (By.CSS_SELECTOR, '')
    DRAG_CENTER = (By.CSS_SELECTOR, '')
    DRAG_LEFT = (By.CSS_SELECTOR, '')
    DRAG_BOTTOM = (By.CSS_SELECTOR, '')


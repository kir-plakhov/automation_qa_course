from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')
    GRID_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    ITEM_GRID = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEM = (By.CSS_SELECTOR, 'ul[id="verticalListContainer"] li[class="mt-2 list-group-item '
                                  'list-group-item-action"]')
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, 'ul[id="verticalListContainer"] li[class="mt-2 list-group-item active '
                                         'list-group-item-action"]')
    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="gridContainer"] li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, 'div[id="gridContainer"] li[class="list-group-item active '
                                         'list-group-item-action"]')


class ResizablePageLocators:
    FIRST_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    SECOND_BOX = (By.CSS_SELECTOR, 'div[id="resizable"]')
    FIRST_BOX_HANDLER = (By.CSS_SELECTOR, 'div[class="constraint-area"] span[class="react-resizable-handle '
                                          'react-resizable-handle-se"]')
    SECOND_BOX_HANDLER = (By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle '
                                           'react-resizable-handle-se"]')


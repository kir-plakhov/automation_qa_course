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


class DroppablePageLocators:
    # Simple tab
    SIMPLE = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    # Accept tab
    ACCEPT = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    # Prevent propogation tab
    PREVENT_PROPOGATION = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, '#ppDropContainer #dragBox')

    # Revert draggable tab
    REVERT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-revertable']")
    WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_HERE_REVERT = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')


class DraggablePageLocators:

    # Simple tab
    SIMPLE = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    DRAG_ME = (By.CSS_SELECTOR, 'div[id="draggableExample-tabpane-simple"] div[id="dragBox"]')

    # Axis tab
    AXIS_RESTRICTED = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    ONLY_Y = (By.CSS_SELECTOR, 'div[id="restrictedY"')

    CONTAINER_RESTRICTED = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-containerRestriction"]')
    CURSOR_STYLE = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-cursorStyle"]')
    CONTAINMENT_WRAPPER = (By.CSS_SELECTOR, 'div[id="containmentWrapper"]')
    WITHIN_THE_BOX = (By.CSS_SELECTOR, 'div[id="containmentWrapper"] div[class="draggable ui-widget-content ui-draggable ui-draggable-handle"]')
    WITHIN_MY_PARENT = (By.CSS_SELECTOR, 'div[class="draggable ui-widget-content m-3"] span[class="ui-widget-header ui-draggable ui-draggable-handle"]')
    CONTAINMENT_2 = (By.CSS_SELECTOR, 'div[class="draggable ui-widget-content m-3"]')


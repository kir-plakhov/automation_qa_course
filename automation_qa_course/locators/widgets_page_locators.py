from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_SECTION = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    FIRST_SECTION_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECOND_SECTION = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECOND_SECTION_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    THIRD_SECTION = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    THIRD_SECTION_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_REMOVE_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')

    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')


class DatePickerPageLocators:
    SELECT_DATE = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_DAY_LIST = (By.CSS_SELECTOR, '[class=""]')
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


class SliderPageLocators:
    SLIDER = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarPageLocators:
    START_STOP_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    BAR_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')


class TabsPageLocators:
    WHAT_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    WHAT_TAB_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    ORIGIN_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    ORIGIN_TAB_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    USE_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    USE_TAB_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')


class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    BUTTON_TOOL_TIP = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    FIELD = (By.XPATH, '//*[@id="toolTipTextField"]')
    FIELD_TOOL_TIP = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    CONTRARY_LINK = (By.XPATH, '//*[.="Contrary"]')
    CONTRARY_LINK_TOOL_TIP = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    SECOND_LINK = (By.XPATH, '//*[.="1.10.32"]')
    SECOND_LINK_TOOL_TIP = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')

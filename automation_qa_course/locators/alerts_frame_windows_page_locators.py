from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")

    # new tab text
    TITLE_NEW_TAB = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    APPEAR_ALERT_IN_FIVE_SECONDS_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    ALERT_WITH_CONFIRMATION_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    ALERT_WITH_PROMPT_BOX_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    CONFIRM_TEXT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_TEXT = (By.CSS_SELECTOR, 'span[id="promptResult"]')


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    FRAME_TITLE = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

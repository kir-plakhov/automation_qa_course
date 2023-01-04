import time

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_new_tab_or_window_is_opened(self, button):
        if button == 'tab':
            self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            text_title = self.element_is_present(self.locators.TITLE_NEW_TAB).text
            return text_title
        elif button == 'window':
            self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            text_title = self.element_is_present(self.locators.TITLE_NEW_TAB).text
            return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_in_five_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_IN_FIVE_SECONDS_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.ALERT_WITH_CONFIRMATION_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_TEXT).text
        return text_result

    def check_prompt_alert(self):
        text = 'Your test successfully passed'
        self.element_is_visible(self.locators.ALERT_WITH_PROMPT_BOX_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_TEXT).text
        return text, text_result

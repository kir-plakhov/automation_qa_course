import time

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramesPageLocators, NestedFramesPageLocators, ModalDialogsPageLocators
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


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_TITLE).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_TITLE).text
            self.driver.switch_to.default_content()
            return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        text_small = self.element_is_visible(self.locators.SMALL_MODAL_TEXT).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        text_large = self.element_is_visible(self.locators.LARGE_MODAL_TEXT).text
        return [title_small, len(text_small)], [title_large, len(text_large)]

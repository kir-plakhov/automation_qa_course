import random
import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:

        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            result = browser_windows_page.check_new_tab_or_window_is_opened('tab')
            assert result == 'This is a sample page', "New tab has not been opened or tab is incorrect"

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            result = browser_windows_page.check_new_tab_or_window_is_opened('window')
            assert result == 'This is a sample page', "New window has not been opened or window is incorrect"

    class TestAlertsPage:

        def test_see_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_alert()
            assert alert_text == 'You clicked a button'

        def test_see_alert_in_five_sec(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_alert_appear_in_five_sec()
            assert alert_text == 'This alert appeared after 5 seconds'

        def test_see_confirm_box(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_confirm_alert()
            assert alert_text == 'You selected Ok'

        def test_prompt_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text, alert_text = alerts_page.check_prompt_alert()
            assert alert_text == f'You entered {text}'

    class TestFramesPage:

        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            result_frame_1 = frames_page.check_frame('frame1')
            result_frame_2 = frames_page.check_frame('frame2')
            assert result_frame_1 == ['This is a sample page', '500px', '350px']
            assert result_frame_2 == ['This is a sample page', '100px', '100px']

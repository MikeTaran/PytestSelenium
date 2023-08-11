import pytest
from pages.frame_page import WindowsTabPage, AlertsPage

url_windows = 'https://demoqa.com/browser-windows'
url_alerts = 'https://demoqa.com/alerts'
url_frames = 'https://demoqa.com/frames'
url_nested_frames = 'https://demoqa.com/nestedframes'
url_modal = 'https://demoqa.com/modal-dialogs'


class TestFrameAlertWindow:
    class TestWindowsTab:
        @pytest.mark.test
        def test_windows_tab(self, driver):
            windows_page = WindowsTabPage(driver, url_windows)
            windows_page.open()
            new_tab_text, text_id, core_tab_url, new_tab_url, number_of_tabs = windows_page.windows_new_tab('tab')
            assert new_tab_text == 'This is a sample page', 'The new tab message is Not correct'
            assert text_id == 'sampleHeading', 'The ID of text message is Not correct'
            assert core_tab_url == url_windows, 'The main tab was Not open'
            assert 'sample' in new_tab_url, 'The URL new tab is Not correct'
            assert number_of_tabs == 2, 'It was opened more or less one tab'

        def test_new_window(self, driver):
            windows_page = WindowsTabPage(driver, url_windows)
            windows_page.open()
            new_tab_text, text_id, core_tab_url, new_tab_url, number_of_tabs = windows_page.windows_new_tab('window')
            assert new_tab_text == 'This is a sample page', 'The new windows message is Not correct'
            assert text_id == 'sampleHeading', 'The ID of text message is Not correct'
            assert core_tab_url == url_windows, 'The main windows was Not open'
            assert 'sample' in new_tab_url, 'The URL new windows is Not correct'
            assert number_of_tabs == 2, 'It was opened more or less one windows'

    class TestAlerts:
        def test_simple_alert(self, driver):
            alerts_page = AlertsPage(driver, url_alerts)
            alerts_page.open()
            alert_text = alerts_page.simple_alert()
            assert alert_text == 'You clicked a button', 'The alert text is Not correct'

        def test_time_alert(self, driver):
            alerts_page = AlertsPage(driver, url_alerts)
            alerts_page.open()
            alert_text = alerts_page.time_alert()
            assert '5 seconds' in alert_text, 'The alert text is Not correct'

        def test_confirm_alerts(self, driver):
            alerts_page = AlertsPage(driver, url_alerts)
            alerts_page.open()
            confirm_text, dismiss_text = alerts_page.confirm_alert()
            assert 'Ok' in confirm_text, 'The confirm text is Not correct'
            assert 'Cancel' in dismiss_text, 'The dismiss text is Not correct'

        def test_prompt_alerts(self, driver):
            alerts_page = AlertsPage(driver, url_alerts)
            alerts_page.open()
            confirm_text, first_name = alerts_page.prompt_alert()
            assert first_name in confirm_text, 'The confirm text is Not correct'

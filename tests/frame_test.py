import allure
import pytest
from pages.frame_page import (WindowsTabPage, AlertsPage, IframesPage, NestedFramePage, ModalDialogPage)

url_windows = 'https://demoqa.com/browser-windows'
url_alerts = 'https://demoqa.com/alerts'
url_iframes = 'https://demoqa.com/frames'
url_nested_iframes = 'https://demoqa.com/nestedframes'
url_modal = 'https://demoqa.com/modal-dialogs'


@allure.suite('Alerts, Frame & Windows')
class TestFrameAlertWindow:
    @allure.feature('Test Browser Windows')
    class TestWindowsTab:
        @allure.title('Check window tabs')
        @pytest.mark.test
        def test_windows_tab(self, driver):
            windows_page = WindowsTabPage(driver, url_windows)
            windows_page.open()
            new_tab_text, text_id, core_tab_url, new_tab_url, number_of_tabs = windows_page.windows_new_tab('tab')
            with allure.step('assert new_tab_text'):
                assert new_tab_text == 'This is a sample page', 'The new tab message is Not correct'
            with allure.step('assert text_id'):
                assert text_id == 'sampleHeading', 'The ID of text message is Not correct'
            with allure.step('assert core_tab_url'):
                assert core_tab_url == url_windows, 'The main tab was Not open'
            with allure.step('assert new_tab_url'):
                assert 'sample' in new_tab_url, 'The URL new tab is Not correct'
            with allure.step('assert number_of_tabs'):
                assert number_of_tabs == 2, 'It was opened more or less one tab'

        @allure.title('Check new window')
        def test_new_window(self, driver):
            windows_page = WindowsTabPage(driver, url_windows)
            windows_page.open()
            new_tab_text, text_id, core_tab_url, new_tab_url, number_of_tabs = windows_page.windows_new_tab('window')
            assert new_tab_text == 'This is a sample page', 'The new windows message is Not correct'
            assert text_id == 'sampleHeading', 'The ID of text message is Not correct'
            assert core_tab_url == url_windows, 'The main windows was Not open'
            assert 'sample' in new_tab_url, 'The URL new windows is Not correct'
            assert number_of_tabs == 2, 'It was opened more or less one windows'

    @allure.feature('Test Alerts')
    class TestAlerts:
        @allure.title('Check simple alerts')
        def test_simple_alert(self, driver):
            alerts_page = AlertsPage(driver, url_alerts)
            alerts_page.open()
            alert_text = alerts_page.simple_alert()
            assert alert_text == 'You clicked a button', 'The alert text is Not correct'

        @allure.title('Check time alerts')
        def test_time_alert(self, driver):
            alerts_page = AlertsPage(driver, url_alerts)
            alerts_page.open()
            alert_text = alerts_page.time_alert()
            assert '5 seconds' in alert_text, 'The alert text is Not correct'

        @allure.title('Check confirm alerts')
        def test_confirm_alerts(self, driver):
            alerts_page = AlertsPage(driver, url_alerts)
            alerts_page.open()
            confirm_text, dismiss_text = alerts_page.confirm_alert()
            assert 'Ok' in confirm_text, 'The confirm text is Not correct'
            assert 'Cancel' in dismiss_text, 'The dismiss text is Not correct'

        @allure.title('Check prompt alerts')
        def test_prompt_alerts(self, driver):
            alerts_page = AlertsPage(driver, url_alerts)
            alerts_page.open()
            confirm_text, first_name = alerts_page.prompt_alert()
            assert first_name in confirm_text, 'The confirm text is Not correct'

    @allure.feature('Test Frames')
    class TestIframes:
        @allure.title('Check frames')
        def test_iframes(self, driver):
            iframes_page = IframesPage(driver, url_iframes)
            iframes_page.open()
            result1 = iframes_page.check_iframe('frame1')
            result2 = iframes_page.check_iframe('frame2')
            assert result1 == ['500px', '350px', 'This is a sample page'], 'The frame is Not exist'
            assert result2 == ['100px', '100px', 'This is a sample page'], 'The frame is Not exist'

    @allure.feature('Test Nested Frames')
    class TestNestedFrames:
        @allure.title('Check nested frames')
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramePage(driver, url_nested_iframes)
            nested_frame_page.open()
            iframe_parent_text, iframe_child_text, iframe_parent_text_return, main_page_text = (nested_frame_page
                                                                                                .check_nested_frames())
            assert iframe_parent_text == 'Parent frame', 'The parent iframe was Not selected'
            assert iframe_child_text == 'Child Iframe', 'The child iframe was Not selected'
            assert iframe_parent_text_return == 'Parent frame', 'The parent iframe was Not selected after return'
            assert 'Sample Nested Iframe page.' in main_page_text, 'The main page was Not selected after return'

    @allure.feature('Test Modal Dialog')
    class TestModalDialogs:
        @allure.title('Check modal dialog')
        @pytest.mark.xfail
        def test_modal_dialog(self, driver):
            modal_dialog_page = ModalDialogPage(driver, url_modal)
            modal_dialog_page.open()
            small_result = modal_dialog_page.check_small_modal_dialogs()
            large_result = modal_dialog_page.check_large_modal_dialogs()
            assert large_result[1] > small_result[1], 'The small modal is bigger large modal'
            assert large_result[0] == 'Large Modal', 'The header is Not "Large Modal"'
            assert small_result[0] == 'Small Modal', 'The header is Not "Small Modal"'

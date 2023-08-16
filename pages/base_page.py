from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
        self.remove_footer_and_banners()

    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                         message=f"Can't see element by locator {locator}")

    def element_is_not_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator),
                                                         message=f"Can see element by locator {locator}")

    def elements_are_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator),
                                                         message=f"Can't see element by locator {locator}")

    def element_is_present(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Element not present by locator {locator}")

    def elements_are_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Elements not present by locator {locator}")

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Can't find elements by locator {locator}")

    def element_is_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator),
                                                         message=f"Can't click element by locator {locator}")

    def go_to_element(self, element):
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", element)

    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    def alert_is_present(self, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        alert = wait.until(EC.alert_is_present(), message=f"Can't find alert")
        return alert

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_drag_and_drop_offset(self, element, x_coord, y_coord):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coord, y_coord)
        action.perform()

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    # remove banners
    def remove_footer_and_banners(self):
        tab_name = self.driver.window_handles[0]
        try:
            self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
            self.driver.execute_script("document.getElementById('close-fixedban').remove();")
            self.driver.execute_script("document.getElementById('adplus-anchor').remove();")
            self.driver.execute_script("document.getElementById('RightSide_Advertisement').remove();")
            self.driver.switch_to.frame(0)
            self.driver.execute_script("document.getElementById('google_image_div').remove();")
            self.driver.switch_to.window(tab_name)
        except:
            self.driver.switch_to.window(tab_name)
        # self.driver.execute_script("document.body.style.zoom = '0.75'")

    def refresh_window(self):
        self.driver.refresh()

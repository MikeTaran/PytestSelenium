import time

from locators.widgets_page_locators import AccordianWidgetsPageLocators
from pages.base_page import BasePage


class AccordianWidgetsPage(BasePage):
    locators = AccordianWidgetsPageLocators()

    def check_accordian_content(self):
        title_data = []
        content_len_data = []
        accord_data = True
        accordian_len = len(self.elements_are_present(self.locators.ACCORDIAN_LIST))
        title_list = self.elements_are_visible(self.locators.ACCORDIAN_TITLE_LIST)
        content_list = self.elements_are_present(self.locators.ACCORDIAN_CONTENT_LIST)
        for i in range(accordian_len):

            title_data.append(title_list[i].text)
            title_list[i].click()
            content = len(content_list[i].text)
            if content == 0:
                title_list[i].click()
                content = len(content_list[i].text)
            content_len_data.append(content)
            # проверка, что одновременно открыта только одна вкладка
            for j in range(accordian_len):
                if j != i:
                    cont = len(content_list[j].text)
                    if cont != 0:
                        accord_data = False
            time.sleep(2)

        return accordian_len, title_data, content_len_data, accord_data

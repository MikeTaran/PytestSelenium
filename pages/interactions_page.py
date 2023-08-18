import random

from selenium.common import TimeoutException

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePagelocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def check_sortable_list(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        elements = self.elements_are_visible(self.locators.LIST_TAB_LIST)
        order_before = self.text_of_elements_list(elements)
        elem_list = random.sample(elements, k=2)
        self.action_drag_and_drop_to_element(elem_list[0], elem_list[1])
        order_after = self.text_of_elements_list(elements)
        return order_before, order_after

    def check_sortable_grid(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        elements = self.elements_are_visible(self.locators.GRID_TAB_LIST)
        order_before = self.text_of_elements_list(elements)
        elem_list = random.sample(elements, k=2)
        self.action_drag_and_drop_to_element(elem_list[0], elem_list[1])
        order_after = self.text_of_elements_list(elements)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def check_selectable_list(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        elements = self.elements_are_visible(self.locators.LIST_TAB_LIST)
        for i in range(5):
            elements[random.randint(0, len(elements) - 1)].click()
        try:
            selected_elements = self.elements_are_visible(self.locators.LIST_TAB_LIST_ACTIVE)
            list_after = self.text_of_elements_list(selected_elements)
            return len(list_after)
        except TimeoutException:
            return 0

    def check_selectable_grid(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        elements = self.elements_are_visible(self.locators.GRID_TAB_LIST)
        for i in range(10):
            elements[random.randint(0, len(elements) - 1)].click()
        try:
            selected_elements = self.elements_are_visible(self.locators.GRID_TAB_LIST_ACTIVE)
            list_after = self.text_of_elements_list(selected_elements)
            return len(list_after)
        except TimeoutException:
            return 0

class ResizablePage(BasePage):
    locators = ResizablePagelocators()
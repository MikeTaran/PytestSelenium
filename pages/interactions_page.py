import random
import time

from selenium.common import TimeoutException

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DraggablePageLocators
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
    locators = ResizablePageLocators()

    @staticmethod
    def get_size_of_element(element):
        size = element.get_attribute("style")
        width = int(size.split(";")[0].split(":")[1].replace(" ", "")[:-2])
        height = int(size.split(";")[1].split(":")[1].replace(" ", "")[:-2])
        return [width, height]

    def check_resizable_restricted(self):
        element1 = self.element_is_visible(self.locators.BOX_1)
        anchor_element1 = self.element_is_present(self.locators.BOX_1_ANCHOR)
        self.action_drag_and_drop_offset(anchor_element1, 350, 250)
        size_max = self.get_size_of_element(element1)
        self.action_drag_and_drop_offset(anchor_element1, -400, -200)
        size_min = self.get_size_of_element(element1)
        return size_max, size_min

    def check_resizable_free(self):
        element1 = self.element_is_visible(self.locators.BOX_2)
        anchor_element1 = self.element_is_present(self.locators.BOX_2_ANCHOR)
        self.action_drag_and_drop_offset(anchor_element1, random.randint(-150, 150), random.randint(-150, 150))
        size_free_box = self.get_size_of_element(element1)
        return size_free_box


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def check_droppable_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag = self.element_is_visible(self.locators.DRAG)
        drop = self.element_is_visible(self.locators.DROP_SIMPLE)
        self.action_drag_and_drop_to_element(drag, drop)
        drop_title = self.element_is_visible(self.locators.DROP_SIMPLE_TITLE).text
        drop_color = self.get_background_color_element_hex(drop)
        return drop_title, drop_color

    def check_droppable_not_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_not_accept = self.element_is_visible(self.locators.DRAG_NOT_ACCEPTABLE)
        drop = self.element_is_visible(self.locators.DROP_ACCEPT)
        self.action_drag_and_drop_to_element(drag_not_accept, drop)
        drop_title = self.element_is_visible(self.locators.DROP_ACCEPT_TITLE).text
        drop_color = self.get_background_color_element_hex(drop)
        return drop_title, drop_color

    def check_droppable_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_accept = self.element_is_visible(self.locators.DRAG_ACCEPTABLE)
        drop = self.element_is_visible(self.locators.DROP_ACCEPT)
        self.action_drag_and_drop_to_element(drag_accept, drop)
        drop_title = self.element_is_visible(self.locators.DROP_ACCEPT_TITLE).text
        drop_color = self.get_background_color_element_hex(drop)
        return drop_title, drop_color

    def check_prevent_not_greedy(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag = self.element_is_visible(self.locators.DRAG_PREVENT)
        outer_not_greedy = self.element_is_visible(self.locators.OUTER_NOT_GREEDY)
        inner_not_greedy = self.element_is_visible(self.locators.INNER_NOT_GREEDY)
        self.action_drag_and_drop_to_element(drag, inner_not_greedy)
        outer_title = self.element_is_visible(self.locators.OUTER_NOT_GREEDY_TITLE).text
        inner_title = self.element_is_visible(self.locators.INNER_NOT_GREEDY_TITLE).text
        outer_color = self.get_background_color_element_hex(outer_not_greedy)
        inner_color = self.get_background_color_element_hex(inner_not_greedy)
        return outer_title, inner_title, outer_color, inner_color

    def check_prevent_greedy(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag = self.element_is_visible(self.locators.DRAG_PREVENT)
        outer_not_greedy = self.element_is_visible(self.locators.OUTER_GREEDY)
        inner_not_greedy = self.element_is_visible(self.locators.INNER_GREEDY)
        self.action_drag_and_drop_to_element(drag, inner_not_greedy)
        outer_title = self.element_is_visible(self.locators.OUTER_GREEDY_TITLE).text
        inner_title = self.element_is_visible(self.locators.INNER_GREEDY_TITLE).text
        outer_color = self.get_background_color_element_hex(outer_not_greedy)
        inner_color = self.get_background_color_element_hex(inner_not_greedy)
        return outer_title, inner_title, outer_color, inner_color

    def check_revert(self):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        drag_revert = self.element_is_visible(self.locators.DRAG_REVERT)
        drop = self.element_is_visible(self.locators.DROP_REVERT)
        self.action_drag_and_drop_to_element(drag_revert, drop)
        drop_title = self.element_is_visible(self.locators.DROP_REVERT_TITLE).text
        drop_color = self.get_background_color_element_hex(drop)
        time.sleep(0.5)
        position = self.get_position_of_element(drag_revert)

        return position, drop_title, drop_color

    def check_not_revert(self):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        drag_revert = self.element_is_visible(self.locators.DRAG_NOT_REVERT)
        drop = self.element_is_visible(self.locators.DROP_REVERT)
        self.action_drag_and_drop_to_element(drag_revert, drop)
        drop_title = self.element_is_visible(self.locators.DROP_REVERT_TITLE).text
        drop_color = self.get_background_color_element_hex(drop)
        time.sleep(0.5)
        position = self.get_position_of_element(drag_revert)

        return position, drop_title, drop_color


class DraggablePage(BasePage):
    locators = DraggablePageLocators()

    def check_draggable_simple(self):
        self.element_is_visible(self.locators.TAB_SIMPLE).click()
        drag = self.element_is_visible(self.locators.DRAG_SIMPLE)
        position_before = self.get_position_of_element(drag)
        shift_x = random.randint(1, 100)
        shift_y = random.randint(1, 100)
        self.action_drag_and_drop_offset(drag, shift_x, shift_y)
        position_after = self.get_position_of_element(drag)
        return position_before, position_after

    def check_axis_restricted(self):
        self.element_is_visible(self.locators.TAB_AXIS).click()
        drag_x = self.element_is_visible(self.locators.DRAG_X)
        drag_y = self.element_is_visible(self.locators.DRAG_Y)
        position_x_before = self.get_position_of_element(drag_x)
        position_y_before = self.get_position_of_element(drag_y)
        shift_x = random.randint(1, 100)
        shift_y = random.randint(1, 100)
        self.action_drag_and_drop_offset(drag_x, shift_x, shift_y)
        self.action_drag_and_drop_offset(drag_y, shift_x, shift_y)
        position_x_after = self.get_position_of_element(drag_x)
        position_y_after = self.get_position_of_element(drag_y)
        return position_x_before, position_x_after, position_y_before, position_y_after

    def check_container_restricted_box(self):
        self.element_is_visible(self.locators.TAB_CONTAINER).click()
        drag = self.element_is_visible(self.locators.DRAG_CONTAINED)
        box = self.element_is_visible(self.locators.BOX_CONTAINER)
        drag_size = self.get_size_of_element(drag)
        box_size = self.get_size_of_element(box)
        shift_x = box_size[0] - drag_size[0] + 150
        shift_y = box_size[1] - drag_size[1] + 150
        self.action_drag_and_drop_offset(drag, shift_x, shift_y)
        drag_position = self.get_position_of_element(drag)
        time.sleep(3)
        return drag_position, box_size

    def check_container_restricted_parent(self):
        self.element_is_visible(self.locators.TAB_CONTAINER).click()
        drag = self.element_is_visible(self.locators.SPAN_CONTAINED)
        box = self.element_is_visible(self.locators.PARENT_CONTAINER)
        box_size = self.get_size_of_element(box)
        shift_x = box_size[0] + 50
        shift_y = box_size[1] + 50
        self.action_drag_and_drop_offset(drag, shift_x, shift_y)
        drag_position = self.get_position_of_element(drag)
        time.sleep(3)
        return drag_position, box_size

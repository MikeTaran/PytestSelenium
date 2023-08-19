import time

import pytest

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage

url_sortable = 'https://demoqa.com/sortable'
url_selectable = 'https://demoqa.com/selectable'
url_resizable = 'https://demoqa.com/resizable'
url_droppable = 'https://demoqa.com/droppable'
url_dragabble = 'https://demoqa.com/dragabble'


class TestInteractions:
    class TestSortable:
        def test_sortable_list(self, driver):
            sortable_page = SortablePage(driver, url_sortable)
            sortable_page.open()
            order_before, order_after = sortable_page.check_sortable_list()
            assert order_before != order_after, 'Sortable list was Not changed'

        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, url_sortable)
            sortable_page.open()
            order_before, order_after = sortable_page.check_sortable_grid()
            assert order_before != order_after, 'Sortable grid was Not changed'

    class TestSelectable:
        def test_selectable_list(self, driver):
            selectable_page = SelectablePage(driver, url_selectable)
            selectable_page.open()
            len_selected_elements = selectable_page.check_selectable_list()
            assert len_selected_elements > 0, 'No one list element was selected'

        def test_selectable_grid(self, driver):
            selectable_page = SelectablePage(driver, url_selectable)
            selectable_page.open()
            len_selected_elements = selectable_page.check_selectable_grid()
            assert len_selected_elements > 0, 'No one grid element was selected'
            time.sleep(3)

    class TestResizable:
        @pytest.mark.xfail
        def test_resizable_restricted(self, driver):
            resizable_page = ResizablePage(driver, url_resizable)
            resizable_page.open()
            size_max, size_min = resizable_page.check_resizable_restricted()
            assert size_max == [500, 300], 'Size of element more than restricted'
            assert size_min == [150, 150], 'Size of element less than restricted'

        def test_resizable_free(self, driver):
            resizable_page = ResizablePage(driver, url_resizable)
            resizable_page.open()
            size = resizable_page.check_resizable_free()
            assert size != [200, 200], 'Size of element was Not changed'

    class TestDroppable:
        @staticmethod
        def open_droppable_page(driver):
            droppable_page = DroppablePage(driver, url_droppable)
            droppable_page.open()
            return droppable_page

        def test_droppable_simple(self, driver):
            droppable_page = self.open_droppable_page(driver)
            drop_title, drop_color = droppable_page.check_droppable_simple()
            assert drop_title == 'Dropped!' and drop_color == '#4682b4', 'The element was Not droppable'

        def test_droppable_accept(self, driver):
            droppable_page = self.open_droppable_page(driver)
            drop_title, drop_color = droppable_page.check_droppable_accept()
            assert drop_title == 'Dropped!' and drop_color == '#4682b4', 'The element was Not droppable'

        def test_droppable_not_accept(self, driver):
            droppable_page = self.open_droppable_page(driver)
            drop_title, drop_color = droppable_page.check_droppable_not_accept()
            assert drop_title == 'Drop here' and drop_color == '#000000', 'The element was Not droppable'

        def test_prevent_not_greedy(self, driver):
            droppable_page = self.open_droppable_page(driver)
            outer_title, inner_title, outer_color, inner_color = droppable_page.check_prevent_not_greedy()
            assert (outer_title == 'Dropped!' and inner_title == 'Dropped!' and
                    outer_color == '#4682b4' and inner_color == '#4682b4'), 'Propagation is greedy'

        def test_prevent_greedy(self, driver):
            droppable_page = self.open_droppable_page(driver)
            outer_title, inner_title, outer_color, inner_color = droppable_page.check_prevent_greedy()
            assert (outer_title == 'Outer droppable' and inner_title == 'Dropped!' and
                    outer_color == '#000000' and inner_color == '#4682b4'), 'Propagation is Not greedy'

        def test_revert(self, driver):
            droppable_page = self.open_droppable_page(driver)
            position, drop_title, drop_color = droppable_page.check_revert()
            assert (drop_title == 'Dropped!' and position == ['0px', '0px'] and
                    drop_color == '#4682b4'), 'The element was Not reverted'

        def test_not_revert(self, driver):
            droppable_page = self.open_droppable_page(driver)
            position, drop_title, drop_color = droppable_page.check_not_revert()
            assert (drop_title == 'Dropped!' and position != ['0px', '0px'] and
                    drop_color == '#4682b4'), 'The element was reverted'

    class TestDraggable:
        @staticmethod
        def open_draggable_page(driver):
            draggable_page = DraggablePage(driver, url_dragabble)
            draggable_page.open()
            return draggable_page

        def test_draggable_simple(self, driver):
            draggable_page = self.open_draggable_page(driver)
            position_before, position_after = draggable_page.check_draggable_simple()
            assert position_after != position_before, 'The element didnt move'

        def test_axis_restricted(self, driver):
            draggable_page = self.open_draggable_page(driver)
            position_x_before, position_x_after, position_y_before, position_y_after \
                = draggable_page.check_axis_restricted()
            assert (position_x_after[0] != position_x_before[0] and
                    position_x_after[1] == position_x_before[1]), 'The element was shifted by Y'
            assert (position_y_after[0] == position_y_before[0] and
                    position_y_after[1] != position_y_before[1]), 'The element was shifted by Y'

        def test_container_restricted_box(self, driver):
            draggable_page = self.open_draggable_page(driver)
            drag_position, box_size = draggable_page.check_container_restricted_box()
            assert drag_position[0] < box_size[0] and drag_position[1] < box_size[1], \
                'The element is Not within the box'

        def test_container_restricted_parent(self, driver):
            draggable_page = self.open_draggable_page(driver)
            drag_position, box_size = draggable_page.check_container_restricted_parent()
            assert drag_position[0] < box_size[0] and drag_position[1] < box_size[1], \
                'The element is Not within the box'

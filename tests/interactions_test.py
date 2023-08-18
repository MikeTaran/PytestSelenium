import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage

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
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, url_resizable)
            resizable_page.open()
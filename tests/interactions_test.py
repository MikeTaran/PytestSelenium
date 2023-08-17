from pages.interactions_page import SortablePage

url_sortable = 'https://demoqa.com/sortable'
url_selectable = 'https://demoqa.com/selectable'
url_resizable = 'https://demoqa.com/resizable'
url_droppable = 'https://demoqa.com/droppable'
url_dragabble = 'https://demoqa.com/dragabble'


class TestInteractions:
    class TestSortable:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, url_sortable)
            sortable_page.open()

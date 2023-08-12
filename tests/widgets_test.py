from pages.widgets_page import AccordianWidgetsPage

url_accordian = 'https://demoqa.com/accordian'


class TestWidgets:
    class TestAccordian:
        def test_accordian(self, driver):
            widget_page = AccordianWidgetsPage(driver, url_accordian)
            widget_page.open()
            accordian_len, title, content, accord = widget_page.check_accordian_content()
            title_mockup = ['What is Lorem Ipsum?', 'Where does it come from?', 'Why do we use it?']
            for i in range(accordian_len):
                assert content[i] != 0, f'The block_{i} is empty'
                assert title[i] == title_mockup[i], f'The title of block_{i} is Not correct'
            assert accord, 'More than one block was opened'


import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


class TestInteractions:
    class TestSortablePage:

        def test_sortable_tab(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before, after = sortable_page.change_list_order()
            assert before != after

        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before, after = sortable_page.change_grid_order()
            assert before != after

    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            grid_list = selectable_page.select_grid_item()
            assert len(item_list) > 0
            assert len(grid_list) > 0

    class TestResizablePage:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            #time.sleep(3)
            max_box, min_box = resizable_page.change_size_first_box()
            max_resize, min_resize = resizable_page.change_size_second_box()
            assert ('500px', '300px') == max_box, "maximum size not equal to '500px', '300px'"
            assert ('150px', '150px') == min_box, "minimum size not equal to '150px', '150px'"
            assert min_resize != max_resize, "resizable has not been changed"

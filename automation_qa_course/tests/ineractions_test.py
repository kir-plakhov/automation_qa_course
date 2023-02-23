import time

from automation_qa_course.pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage

from automation_qa_course.pages.interactions_page import DraggablePage


class TestInteractions:
    class TestSortablePage:

        def test_sortable_tab(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before, after = sortable_page.change_list_order()
            assert before != after, "The order of elements has not been changed"

        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before, after = sortable_page.change_grid_order()
            assert before != after, "The order of elements has not been changed"

    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            grid_list = selectable_page.select_grid_item()
            assert len(item_list) > 0, "no elements were selected"
            assert len(grid_list) > 0, "no elements were selected"

    class TestResizablePage:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            time.sleep(3) # ----------------------------------------- CREATE COUNTER
            max_box, min_box = resizable_page.change_size_first_box()
            max_resize, min_resize = resizable_page.change_size_second_box()
            assert ('500px', '300px') == max_box, "maximum size not equal to '500px', '300px'"
            assert ('150px', '150px') == min_box, "minimum size not equal to '150px', '150px'"
            assert min_resize != max_resize, "resizable has not been changed"

    class TestDroppable:

        def test_simple(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', "the elements has not been dropped"

        def test_accept(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_accept, accept = droppable_page.drop_acceptable()
            assert not_accept == 'Drop here', "the dropped element has been accepted"
            assert accept == 'Dropped!', "the dropped element has not been accepted"

        def test_prevent_propagation(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propagation()
            assert not_greedy == 'Dropped!', "the elements texts has not been changed"
            assert not_greedy_inner == 'Dropped!', "the elements texts has not been changed"
            assert greedy == 'Outer droppable', "the elements texts has not been changed"
            assert greedy_inner == 'Dropped!', "the elements texts has not been changed"

        def test_revert_draggable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            after_drop, after_revert = droppable_page.drop_will_revert_draggable()
            after_drop_second, after_revert_second = droppable_page.drop_not_revert_draggable()
            assert after_drop != after_revert, 'the elements has not reverted'
            assert after_drop_second == after_revert_second, 'the elements has  reverted'

    class TestDraggable:

        def test_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before, after = draggable_page.simple_drag_box()
            assert before != after, "the position of the box has not been changed"

        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            top_x, left_x = draggable_page.axis_restricted_x()
            top_y, left_y = draggable_page.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(
                top_x[1][0]) == 0, "box position has not changed or there has been a shift in the y-axis"
            assert left_x[0][0] != left_x[1][0] and int(
                left_x[1][0]) != 0, "box position has not changed or there has been a shift in the y-axis"
            assert top_y[0][0] != top_y[1][0] and int(
                top_y[1][0]) != 0, "box position has not changed or there has been a shift in the x-axis"
            assert left_y[0][0] == left_y[1][0] and int(
                left_y[1][0]) == 0, "box position has not changed or there has been a shift in the x-axis"

from automation_qa_course.pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, \
    ProgressBarPage, TabsPage, ToolTipsPage, MenuPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'

    class TestAutoComplete:

        def test_multi_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors = auto_complete_page.fill_multi_input()
            colors_result = auto_complete_page.check_color_in_multi()
            assert colors == colors_result, 'the added colors are missing in the input'

        def test_remove_value_from_multi(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_multi_input()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi_input()
            assert count_value_before != count_value_after, "value was not deleted"

        def test_single_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            input_color = auto_complete_page.fill_single_input()
            result_color = auto_complete_page.check_color_in_single_input()
            assert input_color == result_color, 'the added colors are missing in the input'

    class TestDatePickerPage:

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, 'the date has not been changed'

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            assert value_date_before != value_date_after, 'the date and time have not been changed'

    class TestSliderPage:

        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            before, after = slider_page.change_slider_value()
            assert before != after, 'slider value has not been changed'

    class TestProgressBarPage:

        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            before, after = progress_bar_page.change_progress_bar_value()
            assert before != after, 'progress bar value has not been changed'

    class TestTabsPage:

        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            what_button, what_content = tabs_page.check_tabs('What')
            origin_button, origin_content = tabs_page.check_tabs('Origin')
            use_button, use_content = tabs_page.check_tabs('Use')
            assert what_button == 'What' and what_content != 0, 'the tab "what" was not pressed or the text is missing'
            assert origin_button == 'Origin' and origin_content != 0, 'the tab "origin" was not pressed or the text is missing'
            assert use_button == 'Use' and use_content != 0, 'the tab "use" was not pressed or the text is missing'

    class TestToolTips:

        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text = tool_tips_page.check_button_tool_tips()
            assert button_text == 'You hovered over the Button', 'hover missing or incorrect content'

        # This test case periodically crashes
        def test_input_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            input_text = tool_tips_page.check_input_tool_tips()
            assert input_text == 'You hovered over the text field', 'hover missing or incorrect content'

        def test_contrary_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            contrary_text = tool_tips_page.check_contrary_tool_tips()
            assert contrary_text == 'You hovered over the Contrary', 'hover missing or incorrect content'

        def test_second_link_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            second_link_text = tool_tips_page.check_second_link_tool_tips()
            assert second_link_text == 'You hovered over the 1.10.32', 'hover missing or incorrect content'

    class TestMenuPage:

        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3'], "menu items do not exist or have not been selected"















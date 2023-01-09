import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
            {
                'title': self.locators.FIRST_SECTION,
                'content': self.locators.FIRST_SECTION_CONTENT
            },
            'second':
                {
                    'title': self.locators.SECOND_SECTION,
                    'content': self.locators.SECOND_SECTION_CONTENT
                },
            'third':
                {
                    'title': self.locators.THIRD_SECTION,
                    'content': self.locators.THIRD_SECTION_CONTENT
                }
        }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_multi_input(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 11))
        for color in colors:
            multi_input = self.element_is_clickable(self.locators.MULTI_INPUT)
            multi_input.send_keys(color)
            multi_input.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi_input(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_REMOVE_VALUE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_single_input(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        single_input = self.element_is_clickable(self.locators.SINGLE_INPUT)
        single_input.send_keys(color)
        single_input.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single_input(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.SELECT_DATE)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_day(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_day(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_day(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_day(self.locators.DATE_AND_TIME_YEAR_LIST, '2018')
        self.set_day(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_day(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE)
        return value_before, value_after.get_attribute('value')


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.BAR_VALUE).text
        progress_bar_button = self.element_is_clickable(self.locators.START_STOP_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(1, 6))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, name_tab):
        tabs = {
            'What': {
                'title': self.locators.WHAT_TAB,
                'content': self.locators.WHAT_TAB_TEXT
            },
            'Origin': {
                'title': self.locators.ORIGIN_TAB,
                'content': self.locators.ORIGIN_TAB_TEXT
            },
            'Use': {
                'title': self.locators.USE_TAB,
                'content': self.locators.USE_TAB_TEXT
            }
        }
        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        tab_content = self.element_is_visible(tabs[name_tab]['content']).text
        return button.text, len(tab_content)


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
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

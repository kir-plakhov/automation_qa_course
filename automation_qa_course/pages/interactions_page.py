import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_items(self.locators.ITEM_LIST)
        item_list = random.sample(self.elements_are_visible(self.locators.ITEM_LIST), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.ITEM_LIST)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.GRID_LIST).click()
        order_before = self.get_sortable_items(self.locators.ITEM_GRID)
        item_list = random.sample(self.elements_are_visible(self.locators.ITEM_GRID), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.ITEM_GRID)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_from_width_height(self, size_value):
        width = size_value.split(';')[0].split(':')[1].replace(' ', '')
        height = size_value.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_visible(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_first_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.FIRST_BOX_HANDLER), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.FIRST_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.FIRST_BOX_HANDLER), -500, -300)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.FIRST_BOX))
        return max_size, min_size

    def change_size_second_box(self):
        self.scroll_to_the_bottom()
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.SECOND_BOX_HANDLER), random.randint(1, 300), random.randint(1,300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.SECOND_BOX))
        self.scroll_to_the_bottom()
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.SECOND_BOX_HANDLER), random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.SECOND_BOX))
        return max_size, min_size

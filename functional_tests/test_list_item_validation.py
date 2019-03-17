from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
# functional Tests: to see how the application functions fromt he users
# point of view
# Minimum viabel app: Simplest thing we can build that is still useful.

# FT should have a human readale story that we can follow.


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):

        # Edith goes to homepage and accidentally tries to submit
        # an empty list item. She hits on the empty input box.
        self.browser.get(self.live_server_url)

        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # The homepage refreshes and there is an error saying that list
        # items cannot be blank
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))
        # She tries again with some text in the input box, which now works.
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Perversely she now decides to submit blank list items
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # she receives a similar warning on the list page.
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))
        # And She correct it by filling some text in it.
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

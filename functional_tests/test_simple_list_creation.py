# from django.test import LiveServerTestCase
from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# functional Tests: to see how the application functions fromt he users
# point of view
# Minimum viabel app: Simplest thing we can build that is still useful.

# FT should have a human readale story that we can follow.


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check its homepage
        # Instead of localhost:8000, LiveServerTestCase gives us an
        # attribute called live_server_url
        self.browser.get(self.live_server_url)
        # she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item'
                         )
        # She types buy peacock feathers int o a text box
        inputbox.send_keys('Buy peacock feathers')
        # when she hits enter the page updates, and now th page lists
        # "1: Buy peacock feathers" as an item in  a to-do list table
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # There is stil a text box inviting her to add another itemself.
        # She enters a second list :"Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # the page updates again and now shows both lists on her list
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect

        # self.fail('Finish the test!')

        # she visits that URL -  TODO:  list is still There
        # satisfied she goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do lists
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She notices her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now a new user, Francis , comes along to the site.

        # # We use a new browser session to make sure that no information of
        # # Edith's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the homepage. There is no sign of Ediths lists
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item. He is less
        # interesting than Edith
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's lists
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # satisfies they both go bakc to sleep.

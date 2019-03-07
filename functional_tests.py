from selenium import webdriver
import unittest

# functional Tests: to see how the application functions fromt he isers point of view
# Minimum viabel app: Simplest thing we can build that is still useful.


# FT should have a human readale story that we can follow.

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check its homepage
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__== '__main__':
    unittest.main(warnings='ignore')

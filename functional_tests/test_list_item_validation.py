from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest
# functional Tests: to see how the application functions fromt he users
# point of view
# Minimum viabel app: Simplest thing we can build that is still useful.

# FT should have a human readale story that we can follow.


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):

        # Edith goes to homepage and accidentally tries to submit
        # an empty list item. She hits on the empty input box.

        # The homepage refreshes and there is an error saying that list
        # items cannot be blank

        # She tries again with some text in the input box, which now works.

        # Perversely she now decides to submit blank list items

        # she receives a similar warning on the list page.

        # And She correct it by filling some text in it.

        self.fail('write me!')

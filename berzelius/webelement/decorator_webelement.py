# Copyright [2021] [Daniel Garcia <contacto {at} danigarcia.org>]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class DecoratorWebElement(WebElement):
    _webelement: WebElement = None

    def __repr__(self):
        if self._webelement is not None:
            return self._webelement.__repr__()
        else:
            return None

    def __repr__(self):
        return getattr(self._webelement, inspect.stack()[0][3])()

    @property
    def tag_name(self):
        """This element's ``tagName`` property."""
        return getattr(self._webelement, inspect.stack()[0][3])

    @property
    def text(self):
        """The text of the element."""
        return getattr(self._webelement, inspect.stack()[0][3])

    def click(self):
        """Clicks the element."""
        getattr(self._webelement, inspect.stack()[0][3])()

    def submit(self):
        """Submits a form."""
        getattr(self._webelement, inspect.stack()[0][3])()

    def clear(self):
        """Clears the text if it's a text entry element."""
        getattr(self._webelement, inspect.stack()[0][3])()

    def get_attribute(self, name):
        """Gets the given attribute or property of the element.

        This method will first try to return the value of a property with the
        given name. If a property with that name doesn't exist, it returns the
        value of the attribute with the same name. If there's no attribute with
        that name, ``None`` is returned.

        Values which are considered truthy, that is equals "true" or "false",
        are returned as booleans.  All other non-``None`` values are returned
        as strings.  For attributes or properties which do not exist, ``None``
        is returned.

        :Args:
            - name - Name of the attribute/property to retrieve.

        Example::

            # Check if the "active" CSS class is applied to an element.
            is_active = "active" in target_element.get_attribute("class")

        """
        return getattr(self._webelement, inspect.stack()[0][3])(name)

    def get_property(self, name):
        """
        Gets the given property of the element.

        :Args:
            - name - Name of the property to retrieve.

        Example::

            text_length = target_element.get_property("text_length")
        """
        return getattr(self._webelement, inspect.stack()[0][3])(name)

    def is_selected(self):
        """Returns whether the element is selected.

        Can be used to check if a checkbox or radio button is selected.
        """
        return getattr(self._webelement, inspect.stack()[0][3])()

    def is_enabled(self):
        """Returns whether the element is enabled."""
        return getattr(self._webelement, inspect.stack()[0][3])()

    def find_element_by_id(self, id_):
        """Finds element within this element's children by ID.

        :Args:
         - id\_ - ID of child element to locate.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            foo_element = element.find_element_by_id('foo')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(id_)

    def find_elements_by_id(self, id_):
        """Finds a list of elements within this element's children by ID.
        Will return a list of webelements if found, or an empty list if not.

        :Args:
         - id\_ - Id of child element to find.

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = element.find_elements_by_id('foo')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(id_)

    def find_element_by_name(self, name):
        """Finds element within this element's children by name.

        :Args:
         - name - name property of the element to find.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = element.find_element_by_name('foo')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(name)

    def find_elements_by_name(self, name):
        """Finds a list of elements within this element's children by name.

        :Args:
         - name - name property to search for.

        :Returns:
         - list of webelement - a list with elements if any was found.  an
           empty list if not

        :Usage:
            elements = element.find_elements_by_name('foo')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(name)

    def find_element_by_link_text(self, link_text):
        """Finds element within this element's children by visible link text.

        :Args:
         - link_text - Link text string to search for.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = element.find_element_by_link_text('Sign In')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(link_text)

    def find_elements_by_link_text(self, link_text):
        """Finds a list of elements within this element's children by visible link text.

        :Args:
         - link_text - Link text string to search for.

        :Returns:
         - list of webelement - a list with elements if any was found.  an
           empty list if not

        :Usage:
            elements = element.find_elements_by_link_text('Sign In')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(link_text)

    def find_element_by_partial_link_text(self, link_text):
        """Finds element within this element's children by partially visible link text.

        :Args:
         - link_text: The text of the element to partially match on.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = element.find_element_by_partial_link_text('Sign')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(link_text)

    def find_elements_by_partial_link_text(self, link_text):
        """Finds a list of elements within this element's children by link text.

        :Args:
         - link_text: The text of the element to partial match on.

        :Returns:
         - list of webelement - a list with elements if any was found.  an
           empty list if not

        :Usage:
            elements = element.find_elements_by_partial_link_text('Sign')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(link_text)

    def find_element_by_tag_name(self, name):
        """Finds element within this element's children by tag name.

        :Args:
         - name - name of html tag (eg: h1, a, span)

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = element.find_element_by_tag_name('h1')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(name)

    def find_elements_by_tag_name(self, name):
        """Finds a list of elements within this element's children by tag name.

        :Args:
         - name - name of html tag (eg: h1, a, span)

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = element.find_elements_by_tag_name('h1')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(name)

    def find_element_by_xpath(self, xpath):
        """Finds element by xpath.

        :Args:
         - xpath - xpath of element to locate.  "//input[@class='myelement']"

        Note: The base path will be relative to this element's location.

        This will select the first link under this element.

        ::

            myelement.find_element_by_xpath(".//a")

        However, this will select the first link on the page.

        ::

            myelement.find_element_by_xpath("//a")

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = element.find_element_by_xpath('//div/td[1]')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(xpath)

    def find_elements_by_xpath(self, xpath):
        """Finds elements within the element by xpath.

        :Args:
         - xpath - xpath locator string.

        Note: The base path will be relative to this element's location.

        This will select all links under this element.

        ::

            myelement.find_elements_by_xpath(".//a")

        However, this will select all links in the page itself.

        ::

            myelement.find_elements_by_xpath("//a")

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = element.find_elements_by_xpath("//div[contains(@class, 'foo')]")

        """
        return getattr(self._webelement, inspect.stack()[0][3])(xpath)

    def find_element_by_class_name(self, name):
        """Finds element within this element's children by class name.

        :Args:
         - name: The class name of the element to find.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = element.find_element_by_class_name('foo')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(name)

    def find_elements_by_class_name(self, name):
        """Finds a list of elements within this element's children by class name.

        :Args:
         - name: The class name of the elements to find.

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = element.find_elements_by_class_name('foo')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(name)

    def find_element_by_css_selector(self, css_selector):
        """Finds element within this element's children by CSS selector.

        :Args:
         - css_selector - CSS selector string, ex: 'a.nav#home'

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = element.find_element_by_css_selector('#foo')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(css_selector)

    def find_elements_by_css_selector(self, css_selector):
        """Finds a list of elements within this element's children by CSS selector.

        :Args:
         - css_selector - CSS selector string, ex: 'a.nav#home'

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = element.find_elements_by_css_selector('.foo')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(css_selector)

    def send_keys(self, *value):
        """Simulates typing into the element.

        :Args:
            - value - A string for typing, or setting form fields.  For setting
              file inputs, this could be a local file path.

        Use this to send simple key events or to fill out form fields::

            form_textfield = driver.find_element_by_name('username')
            form_textfield.send_keys("admin")

        This can also be used to set file inputs.

        ::

            file_input = driver.find_element_by_name('profilePic')
            file_input.send_keys("path/to/profilepic.gif")
            # Generally it's better to wrap the file path in one of the methods
            # in os.path to return the actual path to support cross OS testing.
            # file_input.send_keys(os.path.abspath("path/to/profilepic.gif"))

        """
        return getattr(self._webelement, inspect.stack()[0][3])(*value)

    def is_displayed(self):
        """Whether the element is visible to a user."""
        return getattr(self._webelement, inspect.stack()[0][3])()

    @property
    def location_once_scrolled_into_view(self):
        """THIS PROPERTY MAY CHANGE WITHOUT WARNING. Use this to discover
        where on the screen an element is so that we can click it. This method
        should cause the element to be scrolled into view.

        Returns the top lefthand corner location on the screen, or ``None`` if
        the element is not visible.

        """
        return getattr(self._webelement, inspect.stack()[0][3])

    @property
    def size(self):
        """The size of the element."""
        return getattr(self._webelement, inspect.stack()[0][3])

    def value_of_css_property(self, property_name):
        """The value of a CSS property."""
        return getattr(self._webelement, inspect.stack()[0][3])(property_name)

    @property
    def location(self):
        """The location of the element in the renderable canvas."""
        return getattr(self._webelement, inspect.stack()[0][3])

    @property
    def rect(self):
        """A dictionary with the size and location of the element."""
        return getattr(self._webelement, inspect.stack()[0][3])

    @property
    def screenshot_as_base64(self):
        """
        Gets the screenshot of the current element as a base64 encoded string.

        :Usage:
            img_b64 = element.screenshot_as_base64
        """
        return getattr(self._webelement, inspect.stack()[0][3])

    @property
    def screenshot_as_png(self):
        """
        Gets the screenshot of the current element as a binary data.

        :Usage:
            element_png = element.screenshot_as_png
        """
        return getattr(self._webelement, inspect.stack()[0][3])

    def screenshot(self, filename):
        """
        Saves a screenshot of the current element to a PNG image file. Returns
           False if there is any IOError, else returns True. Use full paths in
           your filename.

        :Args:
         - filename: The full path you wish to save your screenshot to. This
           should end with a `.png` extension.

        :Usage:
            element.screenshot('/Screenshots/foo.png')
        """
        return getattr(self._webelement, inspect.stack()[0][3])(filename)

    @property
    def parent(self):
        """Internal reference to the WebDriver instance this element was found from."""
        return getattr(self._webelement, inspect.stack()[0][3])

    @property
    def id(self):
        """Internal ID used by selenium.

        This is mainly for internal use. Simple use cases such as checking if 2
        webelements refer to the same element, can be done using ``==``::

            if element1 == element2:
                print("These 2 are equal")

        """
        return getattr(self._webelement, inspect.stack()[0][3])

    def __eq__(self, element):
        return getattr(self._webelement, inspect.stack()[0][3])(element)

    def __ne__(self, element):
        return getattr(self._webelement, inspect.stack()[0][3])(element)

    def find_element(self, by=By.ID, value=None):
        """
        Find an element given a By strategy and locator. Prefer the find_element_by_* methods when
        possible.

        :Usage:
            element = element.find_element(By.ID, 'foo')

        :rtype: WebElement
        """
        return getattr(self._webelement, inspect.stack()[0][3])(by, value)

    def find_elements(self, by=By.ID, value=None):
        """
        Find elements given a By strategy and locator. Prefer the find_elements_by_* methods when
        possible.

        :Usage:
            element = element.find_elements(By.CLASS_NAME, 'foo')

        :rtype: list of WebElement
        """
        return getattr(self._webelement, inspect.stack()[0][3])(by, value)

    def __hash__(self):
        return getattr(self._webelement, inspect.stack()[0][3])()

    def _upload(self, filename):
        try:
            return getattr(self._webelement, inspect.stack()[0][3])(filename)
        except Exception as e:
            raise e

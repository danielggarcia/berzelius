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
from berzelius.util.webfinder import WebFinder


class DynamicWebElement:
    """
    Stores information about a WebElement that is not present on Page Load.
    Once the WebElement is present in the web page, locate() method must be invoked, and the DynamicWebElement instance
    must be replaced with an actual WebElement instance.
    """
    _locator: str = ""
    _seeker = None

    def __init__(self, locator: str, seeker):
        """
        Creates a new DynamicWebElement, storing the needed information to create a new WebElement instance
        :param locator: locator to look for. If a string is provided, the search will be performed by default by XPATH.
                        It may be an object with the parameters "by" ("xpath", "id", "name", "class_name", "link_text",
                        "partial_link_text" or "tag_name") an "locator" (the locator string itself)
        :param seeker: webdriver or webelement that will perform the search
        """
        if seeker is not None:
            self._seeker = seeker
        if locator is not None:
            self._locator = locator

    @staticmethod
    def empty():
        """
        Tells PageObjectFactory that the WebElement is Dynamic and it must not be instantiated on startup.
        :return: "DynamicWebElement" string
        """
        return "DynamicWebElement"

    def locate(self):
        """
        Returns a WebElement from the information previously stored in _locator and _seeker attributes.
        The goal of this method is to replace the instance of the DynamicWebElement with an actual WebElement once
        it is instantiated
        :return: WebElement instance from previously stored information
        """
        if self._locator is not None and self._seeker is not None and WebFinder.is_webelement_present(self._locator, self._seeker):
            webelement = WebFinder.find_webelement(self._locator, self._seeker)
            return webelement
        return None


    def get_locator(self):
        """
        Provides the _locator attribute of the Dynamic WebElement
        :return: _locator attribute of the Dynamic WebElement
        """
        return self._locator

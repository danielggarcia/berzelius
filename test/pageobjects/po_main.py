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
from selenium.webdriver.remote.webelement import WebElement

from berzelius.exception.webelement_not_found_exception import WebElementNotFoundException
from berzelius.page.fragment import Fragment
from berzelius.webelement.dynamic_webelement import DynamicWebElement
from berzelius.page.pageobject import PageObject


class POMain(PageObject):
    """
    test.pageobjects.POMain class maps attributes stored in the file definitions.pageobjects.POMain.yaml
    Private attributes, like '__we_txt_search' will match attributes with the same name in the .yaml file, but
    omitting leading underscores. Thus, '__we_txt_search' attribute will be populated with the information stored
    in 'we_txt_search'.
    WebElements are populated by PageObjectFactory, reading the definition file and searching for them in runtime.
    DynamicWebElements, on the other hand, must be initialized by invoking DynamicWebElement.empty(). A WebElement is
    dynamic when it is not present in the DOM when the page (i.e. the rows of a table populated with an Ajax request
    when a button is pressed)
    """
    #region WebElements
    __we_txt_search: WebElement = None
    __we_btn_search: WebElement = None
    __dwe_li_talk: WebElement = DynamicWebElement.empty()
    #endregion

    #region Fragments
    __f_sidebar: Fragment = None
    #endregion

    def enter_text(self, text: str):
        self.set_text(self.__we_txt_search, text)

    def search(self, text: str):
        self.enter_text(text)
        self.__we_btn_search.click()

    def click_discussion(self):
        discussion_link = self.__we_li_talk.locate()
        if discussion_link is not None:
            self.__we_li_talk = discussion_link
            self.__we_li_talk.click()
        else:
            raise WebElementNotFoundException("Can't locate dynamic element {}".format(self.__we_li_talk.get_locator()))

    def goto_main(self):
        self.__f_sidebar.goto_main()

    def show_titles(self):
        self.__f_sidebar.show_titles()

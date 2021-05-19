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

from berzelius.page.fragment import Fragment
from berzelius.page.pageobject import PageObject


class POMain(PageObject):
    #region WebElements
    __we_txt_search: WebElement = None
    __we_btn_search: WebElement = None
    #endregion

    #region Fragments
    __f_sidebar: Fragment = None
    #endregion

    def enter_text(self, text: str):
        self.set_text(self.__we_txt_search, text)

    def search(self, text: str):
        self.enter_text(text)
        self.__we_btn_search.click()

    def goto_main(self):
        self.__f_sidebar.goto_main()

    def show_titles(self):
        self.__f_sidebar.show_titles()
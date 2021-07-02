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

from berzelius.page.fragment import Fragment
from selenium.webdriver.remote.webelement import WebElement


class FragmentDropdown(Fragment):

    #region Attributes
    __is_expanded: bool = False
    #endregion

    #region WebElements
    __w_link_toggle: WebElement = None
    __wa_link_elements: [] = None
    #endregion

    #region Methods

    def get_link_by_title(self, title: str, exact_match: bool = True):
        result = None
        if self.__wa_link_elements is None or len(self.__wa_link_elements) == 0:
            return None
        if exact_match:
            result = list(filter(lambda we: we.text == title), self.__wa_link_elements)
        else:
            result = list(filter(lambda we: title.lower() in we.text.lower() == title), self.__wa_link_elements)
        if result is not None and len(result) > 0:
            return result[0]

    #endregion
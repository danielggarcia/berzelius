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

    #region Fragments
    __fragment_banner: Fragment = None
    '''
    __fragment_topmenu: Fragment = None
    __fragment_carousel: Fragment = None
    __fragment_sidemenu: Fragment = None
    __fragment_board: Fragment = None
    __fragment_footer: Fragment = None
    '''
    #endregion

    #region Methods
    def sponsor_click(self):
        self.__fragment_banner.sponsor_click()
    #endregion
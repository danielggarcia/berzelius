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


class FragmentBanner(Fragment):

    #region WebElements
    __w_link_home: WebElement = None
    __w_img_logo: WebElement = None
    __w_txt_sitename: WebElement = None
    __w_txt_slogan: WebElement = None
    __w_link_sponsor: WebElement = None
    #endregion

    #region Methods

    def logo_click(self):
        self.__w_link_home.click()

    def sponsor_click(self):
        self.__w_link_sponsor.click()

    def get_site_name(self):
        return self.__w_txt_sitename.text

    def get_slogan_text(self):
        return self.__w_txt_slogan.text

    def get_logo_image_source(self):
        return self.__w_img_logo.get_attribute('src')

    #endregion
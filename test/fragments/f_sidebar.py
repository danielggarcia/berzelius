# Copyright [2021] [Daniel Garcia <contacto {at} danigarcia.org]
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


class FSidebar(Fragment):
    __we_link_logo: WebElement = None

    __f_section_contribute: Fragment
    __f_section_tools: Fragment
    __f_section_print_export: Fragment
    __f_section_languages: Fragment

    def goto_main(self):
        self.__we_link_logo.click()

    def show_titles(self):
        print(self.__f_section_contribute.get_title())
        print(self.__f_section_tools.get_title())
        print(self.__f_section_print_export.get_title())
        print(self.__f_section_languages.get_title())
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
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from berzelius.page.webobject import WebObject


class Fragment(WebObject):
    root_webelement: WebElement = None

    def __init__(self, driver: WebDriver, definition: dict, root_webelement: WebElement):
        self._driver = driver
        self._action_chains = ActionChains(self._driver)
        self._definition = definition
        self.root_webelement = root_webelement

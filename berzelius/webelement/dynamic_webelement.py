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
from selenium.webdriver.common.by import By
from berzelius.util.webfinder import WebFinder
from berzelius.webelement.decorator_webelement import DecoratorWebElement


class DynamicWebElement(DecoratorWebElement):
    _locator: str = ""
    _locate_by: By = ""
    _seeker = None

    @property
    def is_located(self):
        return self._locator is not None and self._locate_by is not None and self._webelement is not None

    #TODO Test this
    def __init__(self, locator: str, seeker, locate_by: By=By.XPATH):
        if seeker is not None:
            self._seeker = seeker
        if locator is not None:
            self._locator = locator
        if locate_by is not None:
            self._locate_by = locate_by

    def locate(self):
        if self._locator is not None and self._locate_by is not None:
            locator = {"by": self._locate_by, "locator": self._locator}
            if WebFinder.is_webelement_present(locator, self._seeker):
                self._webelement = WebFinder.find_webelement(locator, self._seeker)
                self._is_located = True
                return True
        return False

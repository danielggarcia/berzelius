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
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from berzelius.util.log_setup import logger

class WebObject:
    _driver: WebDriver
    _action_chains: ActionChains
    _definition: dict

    def get_webelement_definitions(self):
        try:
            if self._definition is not None and "webelements" in self._definition:
                return self._definition['webelements']
            else:
                return {}
        except Exception as e:
            logger.exception(__class__.__name__)
            raise e

    def get_fragment_definitions(self):
        try:
            if self._definition is not None and "fragments" in self._definition:
                return self._definition['fragments']
            else:
                return {}
        except Exception as e:
            logger.exception(__class__.__name__)
            raise e

    def click(self, element: WebElement):
        try:
            element.click()
        except Exception as e:
            logger.exception(__class__.__name__)
            raise e

    def set_text(self, element: WebElement, text: str, clear: bool = True):
        try:
            if clear:
                element.clear()
            element.send_keys(text)
        except Exception as e:
            logger.exception(__class__.__name__)
            raise e

    def double_click(self, element: WebElement):
        try:
            if self._action_chains is None:
                self._action_chains = ActionChains(self._driver)
            self._action_chains.double_click(element).perform()
        except Exception as e:
            logger.exception(__class__.__name__)
            raise e

    def click_and_hold(self, element: WebElement, timeout_ms: int = None):
        try:
            if self._action_chains is None:
                self._action_chains = ActionChains(self._driver)
            self._action_chains.click_and_hold(element).perform()
            if timeout_ms is not None:
                time.sleep(timeout_ms/1000)
                self._action_chains.release(element).perform()
        except Exception as e:
            logger.exception(__class__.__name__)
            raise e

    def release_click(self, element:WebElement):
        try:
            if self._action_chains is None:
                self._action_chains = ActionChains(self._driver)
            self._action_chains.release(element).perform()
        except Exception as e:
            logger.exception(__class__.__name__)
            raise e

    def drag_and_drop(self, element_from: WebElement, element_to: WebElement):
        try:
            #css_script = ".dot { background: red; position: absolute; width: 2px; height: 2px; z-index: 10000; }"
            #js_script = "(function() { \"use strict\"; document.onmousemove = handleMouseMove; function handleMouseMove(event) { var dot, eventDoc, doc, body, pageX, pageY; event = event || window.event; if (event.pageX == null && event.clientX != null) { eventDoc = (event.target && event.target.ownerDocument) || document; doc = eventDoc.documentElement; body = eventDoc.body; event.pageX = event.clientX + (doc && doc.scrollLeft || body && body.scrollLeft || 0) - (doc && doc.clientLeft || body && body.clientLeft || 0); event.pageY = event.clientY + (doc && doc.scrollTop  || body && body.scrollTop  || 0) - (doc && doc.clientTop  || body && body.clientTop  || 0 ); } dot = document.createElement('div'); dot.className = \"dot\"; dot.style.left = event.pageX + \"px\"; dot.style.top = event.pageY + \"px\"; document.body.appendChild(dot); } })();"
            #self._driver.execute_script('document.styleSheets[1].insertRule("' + css_script + '", 0)')
            #self._driver.execute_script(js_script)

            if self._action_chains is None:
                self._action_chains = ActionChains(self._driver)
            self._action_chains.drag_and_drop(element_from, element_to).perform()
        except Exception as e:
            logger.exception(__class__.__name__)
            raise e

    def scroll_down(self, pixels: int = 200):
        self._driver.execute_script("window.scrollBy(0, {}})".format(pixels))

    def get_absolute_center_point_coordinates__(self, element: WebElement):
        try:
            top = int(element.get_attribute("offsetTop"))
            left = int(element.get_attribute("offsetLeft"))
            height = int(element.size["height"])
            width = int(element.size["width"])
            return (left + int(width/2), top + int(height/2))
        except Exception as e:
            logger.exception(__class__.__name__)
            raise e
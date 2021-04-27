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
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from core.exception.webelement_not_found_exception import WebElementNotFoundException
from core.util.log_setup import logger


class WebFinder:
    @staticmethod
    def find_webelement(locator, driver: WebDriver, wait_secs: int = None):
        """
        Finds a webelement in the current page from a locator
        :param locator: locator to look for. If a string is provided, the search will be performed by default by XPATH.
                        It may be an object with the parameters "by" ("xpath", "id", "name", "class_name", "link_text",
                        "partial_link_text" or "tag_name") an "locator" (the locator string itself)
        :param driver: webdriver that will perform the search
        :param wait_secs: timeout to wait the presence of the webelement
        :return: reference to the web element
        """
        try:
            locate_by = By.XPATH
            if type(locator) is dict:
                str_locator = locator["locator"]
                if "by" not in locator or "locator" not in locator:
                    raise Exception("Object definition format mismatch: {}".format(locator))
                if locator["by"].lower() == "id":
                    locate_by = By.ID
                elif locator["by"].lower() == "name":
                    locate_by = By.NAME
                elif locator["by"].lower() == "class_name" or locator["by"].lower() == "classname":
                    locate_by = By.CLASS_NAME
                elif "css" in locator["by"].lower():
                    locate_by = By.CSS_SELECTOR
                elif locator["by"].lower() == "link_text" or locator["by"].lower() == "linktext":
                    locate_by = By.LINK_TEXT
                elif locator["by"].lower() == "partial_link_text" or locator["by"].lower() == "partiallinktext":
                    locate_by = By.PARTIAL_LINK_TEXT
                elif locator["by"].lower() == "tag_name" or locator["by"].lower() == "tag_name":
                    locate_by = By.TAG_NAME
            else:
                str_locator = locator

            # TODO: check driver wait
            wait_time = driver.capabilities['timeouts']['implicit'] if wait_secs is None else wait_secs
            webelements = WebDriverWait(driver, wait_time).until(
                expected_conditions.presence_of_all_elements_located((locate_by, str_locator)))
            if len(webelements) > 0:
                return webelements[0]
            else:
                raise WebElementNotFoundException(locator)
        except WebElementNotFoundException as wenfe:
            logger.exception(__class__.__name__ + "WebElement not found: {}".format(locator))
            raise wenfe
        except Exception as e:
            logger.exception(__class__.__name__ + "WebElement not found: {}".format(locator))
            raise e

    @staticmethod
    def find_webelements(locator, driver: WebDriver, wait_secs: int = None):
        """
        Finds an array webelements in the current page from a locator
        :param locator: locator to look for. If a string is provided, the search will be performed by default by XPATH.
                        It may be an object with the parameters "by" ("xpath", "id", "name", "class_name", "link_text",
                        "partial_link_text" or "tag_name") an "locator" (the locator string itself)
        :param driver: webdriver that will perform the search
        :param wait_secs: timeout to wait the presence of the webelement
        :return: reference to the web element
        """
        try:
            locate_by = By.XPATH
            if type(locator) is dict:
                if "by" not in locator or "locator" not in locator:
                    raise Exception("Object definition format mismatch: {}".format(locator))
                str_locator = locator["locator"]
                if locator["by"].lower() == "id":
                    locate_by = By.ID
                elif locator["by"].lower() == "name":
                    locate_by = By.NAME
                elif locator["by"].lower() == "class_name" or locator["by"].lower() == "classname":
                    locate_by = By.CLASS_NAME
                elif "css" in locator["by"].lower():
                    locate_by = By.CSS_SELECTOR
                elif locator["by"].lower() == "link_text" or locator["by"].lower() == "linktext":
                    locate_by = By.LINK_TEXT
                elif locator["by"].lower() == "partial_link_text" or locator["by"].lower() == "partiallinktext":
                    locate_by = By.PARTIAL_LINK_TEXT
                elif locator["by"].lower() == "tag_name" or locator["by"].lower() == "tag_name":
                    locate_by = By.TAG_NAME
            else:
                str_locator = locator

            # TODO: check driver wait
            wait_time = driver.capabilities['timeouts']['implicit'] if wait_secs is None else wait_secs
            webelements = WebDriverWait(driver, wait_time).until(
                expected_conditions.presence_of_all_elements_located((locate_by, str_locator)))
            if len(webelements) > 0:
                return webelements
            else:
                raise WebElementNotFoundException(locator)
        except WebElementNotFoundException as wenfe:
            logger.exception(__class__.__name__ + "WebElements not found: {}".format(locator))
            raise wenfe
        except Exception as e:
            logger.exception(__class__.__name__ + "WebElements not found: {}".format(locator))
            raise e

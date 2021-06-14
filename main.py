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

import time
from selenium.webdriver.common.keys import Keys
from berzelius.factory.page_object_factory import PageObjectFactory
from berzelius.factory.webdriver_factory import WebDriverFactory
from berzelius.webelement.dynamic_webelement import DynamicWebElement
from berzelius.util.webfinder import WebFinder
from test.tests import TestRunner

def test_webdriver_factory():
    driver = WebDriverFactory.create_instance("chrome")
    driver.get("https://www.google.com")

    time.sleep(5)
    driver.close()

def test_page_object_factory():
    driver = WebDriverFactory.create_instance("firefox")
    #driver.get("https://en.wikipedia.org/wiki/Main_Page")
    driver.get("https://www.google.es")
    try:
        factory = PageObjectFactory(driver)

        time.sleep(3)
        zenlink = DynamicWebElement("//a[contains(text(),'Productos')]", driver)
        agree_btn = WebFinder.find_webelement("//button/div[contains(text(),'Acepto')]/parent::button", driver)
        agree_btn.click()
        txt = WebFinder.find_webelement("//input[@type='text']", driver)
        txt.send_keys("Zennio")
        txt.send_keys(Keys.ENTER)
        zenlink.locate()
        zenlink.click()

        time.sleep(3)
    except Exception as e:
        print(e)
    finally:
        driver.quit()

if __name__ == '__main__':
    #TestRunner.test_webdriverfactory()
    #TestRunner.test_webelements()
    TestRunner.test_webfragments()




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

from core.factory.page_object_factory import PageObjectFactory
from core.factory.webdriver_factory import WebDriverFactory

def test_webdriver_factory():
    driver = WebDriverFactory.create_instance("chrome")
    driver.get("https://www.google.com")

    time.sleep(5)
    driver.close()

def test_page_object_factory():
    driver = WebDriverFactory.create_instance("firefox")
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    factory = PageObjectFactory(driver)
    o = factory.create_instance("test.pageobjects.po_main")
    o.search("binding")

    time.sleep(10)
    driver.close()

if __name__ == '__main__':
    test_page_object_factory()


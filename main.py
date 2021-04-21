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

import os
import time

from selenium import webdriver

from core.enum.browser import Browser
from core.factory.webdriver_factory import WebDriverFactory
from core.util.log_setup import logger
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    '''
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get('https://google.es')
        
    '''


    driver = WebDriverFactory.create_instance()
    driver.get("https://www.google.es")

    time.sleep(2)
    driver.close()



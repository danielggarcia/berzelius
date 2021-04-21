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

from core.factory._chromedriver_factory import _ChromeDriverFactory
from core.factory.browser_options import BrowserOptions
from core.util.log_setup import logger
from core.enum.browser import Browser


class WebDriverFactory:
    __browserProperties = None
    __driver = None

    @staticmethod
    def create_instance(browser: Browser, options: BrowserOptions = None, config_file_path: str = None):
        try:
            if browser == Browser.chrome:
                return _ChromeDriverFactory.create_instance(options, config_file_path)
        except Exception as e:
            logger.exception("WebDriverFactory.create_instance(): error creating instance")
            raise e

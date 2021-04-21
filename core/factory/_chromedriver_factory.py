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
import os.path
import yaml

from core.util.log_setup import logger
from core.factory.browser_options import BrowserOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class _ChromeDriverFactory:
    """
    Internal class that generates a ChromeDriver instance
    """

    @staticmethod
    def __load_default_options(config_file_path:str = None):
        if config_file_path is None:
            cfg_path = os.path.join("config", "chrome_defaults.yaml")
        else:
            cfg_path = config_file_path
        try:
            with open(cfg_path, 'rt') as fd:
                yaml_config = yaml.safe_load(fd.read())
                browser_options = BrowserOptions(yaml_config['driver_executable_path'],
                                                 yaml_config['arguments'],
                                                 yaml_config['experimental_options'],
                                                 yaml_config['binary_path'])
                return browser_options
        except Exception as e:
            logger.exception("Error loading chrome default configuration")
            raise e


    @staticmethod
    def __create_options(options: BrowserOptions = None, config_file_path: str = None):
        try:
            chrome_options = webdriver.ChromeOptions()

            # If None, load default options from config/chrome_defaults.yaml
            # If config file is provided, load data from file
            if options is None or config_file_path is not None:
                options = _ChromeDriverFactory.__load_default_options(config_file_path)

            # Get chromedriver path
            if not os.path.isfile(options.driver_executable_path):
                chrome_options.driver_executable_path = ChromeDriverManager().install()
            else:
                chrome_options.driver_executable_path = options.driver_executable_path

            # Browser binary, if provided
            if os.path.isfile(options.binary_path):
                chrome_options.binary_location = options.binary_path

            # Arguments
            if options.arguments is not None:
                for key in options.arguments:
                    if options.arguments[key] == "":
                        chrome_options.add_argument(key)
                    else:
                        chrome_options.add_argument(key + "=" + options.arguments[key])

            # Experimental options
            if options.experimental_options is not None:
                for key in options.experimental_options:
                    if options.experimental_options[key] == "":
                        chrome_options.add_experimental_option(key, "")
                    else:
                        chrome_options.add_experimental_option(key, options.experimental_options[key])

            return chrome_options

        except Exception as e:
            logger.exception("Error creating Chrome options")
            raise e


    @staticmethod
    def create_instance(options: BrowserOptions = None, config_file_path: str = None):
        """
        Creates a Chrome WebDriver instance based on Browser options or config file in YAML format.
        If no parameters are provided, defaults are loaded from config/chrome_defaults.yaml file.
        If both parameters are provided, config_file_path overrides BrowserOptions configuration.
        :param options: BrowserOptions object with configuration data.
        :param config_file_path: str path to YAML configuration file.
        :return: Chrome WebDriver instance
        """
        chrome_options = _ChromeDriverFactory.__create_options(options)

        try:
            driver = webdriver.Chrome(executable_path=chrome_options.driver_executable_path,
                                      chrome_options=chrome_options,
                                      service_args=["--verbose"])
            return driver

        except WebDriverException as e:
            logger.exception("Error initializing ChromeWebDriver")
            raise e

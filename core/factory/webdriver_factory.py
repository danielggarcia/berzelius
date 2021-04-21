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

import os.path
import yaml
import sys
from core.util.log_setup import logger
from config.configuration import env


class WebDriverFactory:
    __browserProperties = None
    __driver = None

    @staticmethod
    def __load_configuration(config_file_path: str):
        if os.path.exists(config_file_path):
            with open(config_file_path, 'rt') as fd:
                try:
                    driver_config = yaml.safe_load(fd.read())
                    return driver_config
                except Exception as e:
                    logger.exception("Error loading driver configuration from file '{}'".format(config_file_path))
        else:
            raise Exception("Driver configuration file '{}' not found.".format(config_file_path))


    @staticmethod
    def __dynamic_import(modulename, classname):
        module = __import__(modulename, fromlist=[classname])
        target_class = getattr(module, classname)
        return target_class

    @staticmethod
    def __create_factory(driver_configuration: dict):
        try:
            # Extract driver.type field from YAML, and compose the factory name from it using reflection
            # Additional webdriver support can be added just creating additional factories, whose names
            # must match with the format {driver.type}Factory pattern
            factory_name = driver_configuration['driver']['type']

            # Import WebDriver factory dynamically
            webdriver_factory_package = sys.modules[__name__].__package__ + ".webdrivers"
            current_factory_module = webdriver_factory_package + ".{}_factory".format(factory_name.lower())
            current_factory_classname = "{}Factory".format(factory_name)
            factory_class = WebDriverFactory.__dynamic_import(current_factory_module, current_factory_classname)
            factory = factory_class(driver_configuration)
            
            return factory
        except Exception as e:
            logger.exception(__class__.__name__ + ":")


    @staticmethod
    def create_instance(config_file_path: str = None):
        """
        Creates a WebDriver instance by providing a YAML configuration path with configuration parameters
        :param config_file_path: path to YAML configuration file. If not provided, a default instance will be spawned
        loading configuration from config/webdrivers/default.yaml file
        :return: WebDriver instance
        """
        try:
            # Load default driver configuration if not provided
            if config_file_path is None or not os.path.isfile(config_file_path):
                config_file_path = env.get("default_driver_config_file")

            # Generate dictionary from YAML, and create an instance of driver factory
            driver_config = WebDriverFactory.__load_configuration(config_file_path)
            driver_factory = WebDriverFactory.__create_factory(driver_config)

            # Use factory to create a WebDriver instance
            driver = driver_factory.create_instance()

            return driver
        except Exception as e:
            logger.exception(__class__.__name__ + ": error creating instance")
            raise e

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
import os.path

import yaml
import inspect
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from berzelius.webelement.dynamic_webelement import DynamicWebElement
from config.configuration import env
from berzelius.page.pageobject import PageObject
from berzelius.util.webfinder import WebFinder
from berzelius.util.log_setup import logger
from berzelius.util.utils import Utils


class PageObjectFactory:

    def __init__(self, driver: WebDriver = None):
        """
        Creates a new instance of PageObjectFactory
        :param driver: WebDriver that will be assigned to the PageObject
        """
        if driver is None:
            error_message = "Error creating PageObjectFactory: no WebDriver provided"
            logger.error(__class__.__name__ + ": " + error_message)
            raise Exception(error_message)

        self.__driver__ = driver

        self.__definitions_path__ = env.get("definitions_dir")
        if not (os.path.exists(self.__definitions_path__) and os.path.isdir(self.__definitions_path__)):
            error_message = "Error creating PageObjectFactory: definition folder '{}' not found.".format(
                self.__definitions_path__)
            logger.error(__class__.__name__ + ": " + error_message)
            raise Exception(error_message)

    def create_instance(self, object_module: str, root_node: str = None):
        """
        Creates an instance of a PageObject from its object module.
        The factory looks for a .yaml definition file that matches the path of the PageObject inside the 'definitions'
        folder and injects the webelements inside the object based on the XPATH information provided.
        :param object_module: module where the PageObject class is defined
        :return: PageObject instance based on the definition file
        """
        try:
            root_webelement = None
            object_definition = self.__load_object_definition__(object_module)
            if WebFinder.is_webelement_present(root_node, self.__driver__):
                root_webelement = WebFinder.find_webelement(root_node, self.__driver__)
            webobject = self.__create_object__(object_module, object_definition, root_webelement)
            self.__populate_object__(webobject)
            return webobject
        except Exception as e:
            logger.exception(__class__.__name__ + ": Error creating instance.")
            raise e

    def __load_object_definition__(self, object_module: str):
        """
        Loads the content of the definition file and provides a dictionary with the PageObject elements
        Takes the module where the PageObject class is and transforms it in a path with .yaml extension.
        The path of the definition file inside 'definitions' folder MUST match with the path of the mapped module
        in order to define a relation between both elements.
        :param object_module: module of the PageObject to map
        :return: dictionary with the PageObject definition
        """
        try:
            path_elements = object_module.split(".")
            relative_path = os.path.join(*path_elements) + ".yaml"
            relative_path = os.path.join(self.__definitions_path__, relative_path)
            object_configuration = self.__read_definition_file__(relative_path)
            return object_configuration
        except Exception as e:
            logger.exception(__class__.__name__ + ": Error loading object definition.")
            raise e

    def __read_definition_file__(self, path: str):
        """
        Reads the .yaml definition file that contains the Page Object elements and provides a dictionary from it
        :param path: path of the .yaml file
        :return: dictionary containing the elements of the definition file
        """
        values = {}
        try:
            if os.path.exists(path) and os.path.isfile(path):
                with open(path, 'rt') as fd:
                    values = yaml.safe_load(fd.read())
            else:
                raise Exception("File not found")
        except Exception as e:
            logger.exception(__class__.__name__ + ": Error loading PageObject configuration file '{}'".format(path))
            raise e
        return values

    def __create_object__(self, object_module: str, object_definition: dict, root_webelement: WebElement = None):
        """
        Loads dynamically the object class and creates an instance
        :param object_module: module where the class to instantiate is located
        :param object_definition: dictionary with the object definition
        :param root_webelement: parent WebElement of the WebObject
        :return: object instance
        """
        try:
            if object_module is None or object_module == "":
                raise Exception("Object module cannot be empty.")
            if object_definition is None or "classname" not in object_definition:
                raise Exception("'classname' attribute not found in object definition")
            classname = object_definition["classname"]
            classmodule = object_module

            object_class = Utils.dynamic_import(classmodule, classname)
            if root_webelement is None:
                return object_class(self.__driver__, object_definition)
            else:
                return object_class(self.__driver__, object_definition, root_webelement)
        except Exception as e:
            logger.exception(__class__.__name__ + ": Error creating PageObject")
            raise e

    def __populate_object__(self, webobject: PageObject):
        """
        Injects the members of the PageObject from its definitions
        :param webobject: PageObject whose members are going to be injected
        :return: void
        """
        object_content = inspect.getmembers(webobject)
        we_definitions = webobject.get_webelement_definitions()
        fragment_definitions = webobject.get_fragment_definitions()

        # Get webelement instances from 'webelements' definitions
        for e in we_definitions:
            try:
                candidate_webelement = "_{}__{}".format(webobject.__class__.__name__, e)
                if len([attribute for attribute in object_content if candidate_webelement == attribute[0]]) == 1:
                    # If WebObject has a root webelement, the search of the webelement must begin from that webelement
                    # instead from the DOM root node
                    if hasattr(webobject, "root_webelement"):
                        root_node = webobject.root_webelement
                    else:
                        root_node = self.__driver__
                    if isinstance(webobject.__getattribute__(candidate_webelement), str) and webobject.__getattribute__(candidate_webelement) == DynamicWebElement.empty():
                        webelement_instance = DynamicWebElement(we_definitions[e], root_node)
                        webobject.__setattr__(candidate_webelement, webelement_instance)
                    else:
                        webelement_instance = WebFinder.find_webelement(we_definitions[e], root_node)
                        webobject.__setattr__(candidate_webelement, webelement_instance)
            except Exception as e:
                logger.exception(__class__.__name__ + ": Error creating WebElement")
                raise e

        # Get fragment instances from 'fragments' definitions
        for f in fragment_definitions:
            try:
                candidate_fragment = "_{}__{}".format(webobject.__class__.__name__, f)
                if len([attribute for attribute in object_content if candidate_webelement == attribute[0]]) == 1:
                    fragment_module = fragment_definitions[f]["module"]
                    fragment_root_node = fragment_definitions[f]["root_node"]

                    # Call PageObjectFactory recursively to create children fragments from the root node
                    fragment_instance = self.create_instance(fragment_module, fragment_root_node)
                    webobject.__setattr__(candidate_fragment, fragment_instance)
            except Exception as e:
                logger.exception(__class__.__name__ + ": Error creating WebFragment")
                raise e

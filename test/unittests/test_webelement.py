import time
import unittest
from berzelius.factory.page_object_factory import PageObjectFactory
from berzelius.factory.webdriver_factory import WebDriverFactory
from berzelius.util.log_setup import logger

class WebElementTest(unittest.TestCase):

    def setUp(self):
        self.driver = WebDriverFactory.create_instance("firefox")
        self.driver.get("https://www.seleniumeasy.com/test/")
        self.factory = PageObjectFactory(self.driver)
        self.po_main = self.factory.create_instance('test.pageobjects.po_main')

    def tearDown(self):
        self.driver.close()

    def test_static_webelement(self):
        try:
            #self.po_main.search("Bill Gates")
            #self.assertIn("Bill Gates", self.driver.title)
            time.sleep(3)
        except Exception as e:
            logger.exception(__class__.__name__ + ":")

    def test_dynamic_webelement(self):
        try:
            #self.po_main.search("Warren Buffett")
            #self.assertIn("Warren Buffett", self.driver.title)
            #self.po_main.click_discussion()
            #self.assertIn("Disc", self.driver.title)
            time.sleep(3)
        except Exception as e:
            logger.exception(__class__.__name__ + ":")

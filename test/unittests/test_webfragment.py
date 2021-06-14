import time
import unittest
from berzelius.factory.page_object_factory import PageObjectFactory
from berzelius.factory.webdriver_factory import WebDriverFactory
from berzelius.util.log_setup import logger

class WebFragmentTest(unittest.TestCase):

    def setUp(self):
        self.driver = WebDriverFactory.create_instance("firefox")
        self.driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
        self.factory = PageObjectFactory(self.driver)
        self.po_main = self.factory.create_instance('test.pageobjects.po_main')

    def tearDown(self):
        self.driver.close()

    def test_static_webfragment(self):
        try:
            self.po_main.show_titles()
            self.po_main.goto_main()
            time.sleep(5)
        except Exception as e:
            logger.exception(__class__.__name__ + ":")

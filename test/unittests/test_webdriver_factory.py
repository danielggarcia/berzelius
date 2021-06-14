import time
import unittest
from berzelius.factory.webdriver_factory import WebDriverFactory
from berzelius.util.log_setup import logger

class WebDriverFactoryTest(unittest.TestCase):

    def test_chromedriver(self):
        driver = None
        try:
            driver = WebDriverFactory.create_instance("chrome")
            driver.get("https://www.google.com")

            self.assertEqual(driver.title, "Google")
        except Exception as e:
            logger.exception(__class__.__name__ + ":")
        finally:
            driver.close()

    def test_firefoxdriver(self):
        driver = None
        try:
            driver = WebDriverFactory.create_instance("firefox")
            driver.get("https://www.google.com")

            self.assertEqual(driver.title, "Google")
        except Exception as e:
            logger.exception(__class__.__name__ + ":")
        finally:
            driver.close()

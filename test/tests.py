import unittest

from test.unittests.test_webdriver_factory import WebDriverFactoryTest
from test.unittests.test_webelement import WebElementTest
from test.unittests.test_webfragment import WebFragmentTest


class TestRunner:

    @staticmethod
    def test_webdriverfactory():
        suite = unittest.TestSuite()
        suite.addTest(WebDriverFactoryTest('test_chromedriver'))
        suite.addTest(WebDriverFactoryTest('test_firefoxdriver'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    @staticmethod
    def test_webelements():
        suite = unittest.TestSuite()
        suite.addTest(WebElementTest('test_static_webelement'))
        suite.addTest(WebElementTest('test_dynamic_webelement'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    @staticmethod
    def test_webfragments():
        suite = unittest.TestSuite()
        suite.addTest(WebFragmentTest('test_static_webfragment'))

        runner = unittest.TextTestRunner()
        runner.run(suite)
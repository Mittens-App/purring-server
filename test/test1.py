import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys

class MyTestCase(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.browser = webdriver.Firefox(options=options)
        self.addCleanup(self.browser.quit)

    def test_one_func_1(self):
        """
        deffunctiontest1. comments
        """
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)


if __name__ == '__main__':
    print(sys.argv[1])
    unittest.main(verbosity=2)
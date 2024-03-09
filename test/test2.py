import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)
        self.addCleanup(self.browser.quit)

    def test_two_func_1(self):
        """
        Test open googl.
        """
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

    def test_two_func_2(self):
        """
        Test open Yau.
        """
        self.browser.get('http://www.yahoo.cox')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class MyTestCase(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.browser = webdriver.Firefox(options=options)
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        """
        Test open googl.
        """
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

    def test_page_yahoo(self):
        """
        Test open Yau.
        """
        self.browser.get('http://www.yahoo.xcom')
        # self.assertIn('Google', self.browser.title)
        self.fail('gagal ambil cumi2')

    def test_pagii(self):
        """
        Test open xx.
        """
        self.browser.get('https://docs.python.org')
        self.assertEqual('python', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
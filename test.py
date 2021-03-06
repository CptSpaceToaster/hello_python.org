#!/usr/bin/env python3.4
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.python.org')

    def test_python_org_title(self):
        self.assertIn('Python', self.driver.title)

    def test_search_in_python_org(self):
        elem = self.driver.find_element_by_name('q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        self.assertNotIn('No results found.', self.driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

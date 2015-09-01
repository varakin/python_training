# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from kontakt import Kontakt
def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_kontakt(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_kontakt(self):
        self.login(username="admin", password="secret")
        self.fill_new_kontakt(Kontakt(first="qwer", middle="asdf", last="zxcv", phone="1234"))
        self.logout()

    def test_add_empty_kontakt(self):
        wd = self.wd
        self.login(username="admin", password="secret")
        self.fill_new_kontakt(Kontakt(first="", middle="", last="", phone=""))
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def save_new_kontakt(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_new_kontakt(self, kontakt):
        wd = self.wd
        self.open_add_kontakt()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(kontakt.first)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(kontakt.middle)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(kontakt.last)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(kontakt.phone)
        self.save_new_kontakt()
        self.return_home_page()


    def open_add_kontakt(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

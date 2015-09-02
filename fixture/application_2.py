from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session_2 import SessionHelper
from fixture.kontakt import KontaktHelper
__author__ = 'varakin'


class Application_2:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session_2 = SessionHelper(self)
        self.group_2 = KontaktHelper(self)



    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

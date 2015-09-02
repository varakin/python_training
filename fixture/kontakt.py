__author__ = 'varakin'


class KontaktHelper:

    def __init__(self, app):
        self.app = app

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def save_new_kontakt(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_new_kontakt(self, kontakt):
        wd = self.app.wd
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
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe")
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, contact):
        wd = self.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        # return to home page
        self.return_to_home_page()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

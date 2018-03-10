
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        # return to home page
        self.return_to_home_page()

    def fill_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name('selected[]').click()
        # submit deletion
        wd.find_element_by_css_selector("[value='Delete']").click()
        # close alert
        wd.switch_to_alert().accept()
        # return to home page
        self.app.go_to.home_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name('selected[]').click()
        # init edit contact
        wd.find_element_by_css_selector("[title='Edit']").click()
        self.fill_form(contact)
        # submit edit
        wd.find_element_by_name('update').click()
        self.return_to_home_page()


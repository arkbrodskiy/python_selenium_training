
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.app.go_to.home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        # return to home page
        self.return_to_home_page()

    def fill_form(self, contact):
        self.app.utils.change_field_value("firstname", contact.first_name)
        self.app.utils.change_field_value("lastname", contact.last_name)

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.go_to.home_page()
        self.app.utils.select_first()
        # submit deletion
        wd.find_element_by_css_selector("[value='Delete']").click()
        # close alert
        wd.switch_to_alert().accept()
        # return to home page
        self.app.go_to.home_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.go_to.home_page()
        self.app.utils.select_first()
        # init edit contact
        wd.find_element_by_css_selector("[title='Edit']").click()
        self.fill_form(contact)
        # submit edit
        wd.find_element_by_name('update').click()
        self.return_to_home_page()

    def count(self):
        self.app.go_to.home_page()
        self.app.utils.count()

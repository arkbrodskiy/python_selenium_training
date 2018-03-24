from model.contact import Contact


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
        self.contact_cache = None

    def fill_form(self, contact):
        self.app.utils.change_field_value("firstname", contact.first_name)
        self.app.utils.change_field_value("lastname", contact.last_name)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.go_to.home_page()
        self.app.utils.select_by_index(index)
        # submit deletion
        wd.find_element_by_css_selector("[value='Delete']").click()
        # close alert
        wd.switch_to_alert().accept()
        # return to home page
        self.app.go_to.home_page()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.go_to.home_page()
        self.app.utils.select_by_index(index)
        # init edit contact
        wd.find_elements_by_css_selector("[title='Edit']")[index].click()
        self.fill_form(contact)
        # submit edit
        wd.find_element_by_name('update').click()
        self.return_to_home_page()
        self.contact_cache = None

    def count(self):
        self.app.go_to.home_page()
        self.app.utils.count()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.go_to.home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("[name='entry']"):
                last_name = element.find_element_by_css_selector("td:nth-of-type(2)").text
                first_name = element.find_element_by_css_selector("td:nth-of-type(3)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id))
        return self.contact_cache


from model.contact import Contact
import re


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
        self.app.utils.change_field_value("address", contact.address)
        self.app.utils.change_field_value("home", contact.home_phone)
        self.app.utils.change_field_value("mobile", contact.mobile_phone)
        self.app.utils.change_field_value("work", contact.work_phone)
        self.app.utils.change_field_value("phone2", contact.secondary_phone)
        self.app.utils.change_field_value("email", contact.email)
        self.app.utils.change_field_value("email2", contact.email2)
        self.app.utils.change_field_value("email3", contact.email3)

    def create_one_contact(self):
            self.create(Contact(first_name='Created_first_name', last_name='Just_created_last_name',
                                home_phone='5369521475', work_phone='3623652012', mobile_phone='7878756321',
                                secondary_phone='3233653210', email='fgh@ljhg.hg', email2='cvbn@kjgh.rt6',
                                email3='ghkj@ghfc.y', address='765 Drivey Dr., GopTown, GA 76875'))

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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.go_to.home_page()
        self.app.utils.select_by_id(id)
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

    def modify_contact_by_id(self, contact):
        wd = self.app.wd
        self.app.go_to.home_page()
        #self.app.utils.select_by_id(contact.id)
        # init edit contact
        self._click_edit(contact.id)
        #wd.find_elements_by_css_selector("[title='Edit']")[index].click()
        self.fill_form(contact)
        # submit edit
        wd.find_element_by_name('update').click()
        self.return_to_home_page()
        self.contact_cache = None

    def count(self):
        self.app.go_to.home_page()
        return self.app.utils.count()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            self.app.go_to.home_page()
            self.contact_cache = []
            for i in range(self.count()):
                self.contact_cache.append(self.get_contact_from_home_page_by_index(i))
        return self.contact_cache

    def get_contact_from_home_page_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cells = row.find_elements_by_tag_name('td')
        last_name = cells[1].text
        first_name = cells[2].text
        id = row.find_element_by_name("selected[]").get_attribute("value")
        address = cells[3].text
        all_emails = cells[4].text
        all_phones = cells[5].text
        contact = Contact(first_name=first_name, last_name=last_name, id=id, address=address,
                          all_emails_from_home_page=all_emails,
                          all_phones_from_home_page=all_phones)
        return contact


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.go_to.home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.go_to.home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name('firstname').get_attribute('value')
        last_name = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        home_phone = wd.find_element_by_name('home').get_attribute('value')
        work_phone = wd.find_element_by_name('work').get_attribute('value')
        mobile_phone = wd.find_element_by_name('mobile').get_attribute('value')
        secondary_phone = wd.find_element_by_name('phone2').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(first_name=first_name, last_name=last_name, id=id, address=address, home_phone=home_phone,
                       email=email, email2=email2, email3=email3, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone)

    def clear(self, phone):
        return re.sub("[() -]", "", phone)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                (map(lambda x: self.clear(x),
                                     filter(lambda x: x is not None,
                                            [contact.home_phone, contact.mobile_phone,
                                             contact.work_phone, contact.secondary_phone])))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))

    def _click_edit(self, id):
        wd = self.app.wd
        for line in wd.find_elements_by_css_selector("[name='entry']"):
            if len(line.find_elements_by_css_selector("input[value='%s']" % id)) == 1:
                line.find_element_by_css_selector("[title='Edit']").click()
                break


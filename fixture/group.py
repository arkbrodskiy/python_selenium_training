

from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.app.go_to.groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to group page
        self.app.go_to.groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.app.go_to.groups_page()
        self.app.utils.select_by_index(index)
        # submit deletion
        wd.find_element_by_name('delete').click()
        self.app.go_to.groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.app.go_to.groups_page()
        self.app.utils.select_by_id(id)
        # submit deletion
        wd.find_element_by_name('delete').click()
        self.app.go_to.groups_page()
        self.group_cache = None

    def modify_first_group(self, group):
        self.modify_group_by_index(0, group)

    def modify_group_by_index(self, index, group):
        wd = self.app.wd
        self.app.go_to.groups_page()
        self.app.utils.select_by_index(index)
        # init edit group
        wd.find_element_by_name('edit').click()
        self.fill_group_form(group)
        # submit edit
        wd.find_element_by_name('update').click()
        self.app.go_to.groups_page()
        self.group_cache = None

    def modify_group_by_id(self, group):
        wd = self.app.wd
        self.app.go_to.groups_page()
        self.app.utils.select_by_id(group.id)
        # init edit group
        wd.find_element_by_name('edit').click()
        self.fill_group_form(group)
        # submit edit
        wd.find_element_by_name('update').click()
        self.app.go_to.groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.app.utils.change_field_value("group_name", group.name)
        self.app.utils.change_field_value("group_header", group.header)
        self.app.utils.change_field_value("group_footer", group.footer)

    def count(self):
        self.app.go_to.groups_page()
        return self.app.utils.count()

    def create_one_group(self):
        self.create(Group(name='Created_group_name', header='Just_created_header', footer='Fresh_footer'))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.app.go_to.groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)


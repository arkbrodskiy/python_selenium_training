from sys import maxsize

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

    def delete_first_group(self):
        wd = self.app.wd
        self.app.go_to.groups_page()
        self.app.utils.select_first()
        # submit deletion
        wd.find_element_by_name('delete').click()
        self.app.go_to.groups_page()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.app.go_to.groups_page()
        self.app.utils.select_first()
        # init edit group
        wd.find_element_by_name('edit').click()
        self.fill_group_form(group)
        # submit edit
        wd.find_element_by_name('update').click()
        self.app.go_to.groups_page()

    def fill_group_form(self, group):
        self.app.utils.change_field_value("group_name", group.name)
        self.app.utils.change_field_value("group_header", group.header)
        self.app.utils.change_field_value("group_footer", group.footer)

    def count(self):
        self.app.go_to.groups_page()
        return self.app.utils.count()

    def get_group_list(self):
        wd = self.app.wd
        self.app.go_to.groups_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups

    def id_or_max(self, group):
        if group.id:
            return int(group.id)
        else:
            return maxsize

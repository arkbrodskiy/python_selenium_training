

class Go_to:

    def __init__(self, app):
        self.app = app

    def groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('group.php') and len(wd.find_elements_by_name('new')) > 0):
            wd.find_element_by_link_text("groups").click()

    def home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('addressbook/') and len(wd.find_elements_by_name('add')) > 0):
            wd.find_element_by_link_text("home").click()

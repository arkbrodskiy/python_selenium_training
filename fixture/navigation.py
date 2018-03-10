

class Go_to:

    def __init__(self, app):
        self.app = app

    def groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
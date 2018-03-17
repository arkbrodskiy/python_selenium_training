
class Utils:

    def __init__(self, app):
        self.app = app

    def select_first(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

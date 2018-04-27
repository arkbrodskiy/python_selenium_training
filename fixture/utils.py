from sys import maxsize


class Utils:

    def __init__(self, app):
        self.app = app

    def select_first(self):
        self.select_by_index(0)

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def select_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name('selected[]'))

    def id_or_max(self, model_object):
        if model_object.id:
            return int(model_object.id)
        else:
            return maxsize

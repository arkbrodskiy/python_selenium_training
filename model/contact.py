

class Contact:

    def __init__(self, first_name=None, last_name=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "%s %s: %s" % (self.first_name, self.last_name, self.id)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and\
               self.first_name == other.first_name and self.last_name == other.last_name


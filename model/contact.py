

class Contact:

    def __init__(self, first_name=None, last_name=None, id=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None, address=None, email=None, email2=None, email3=None,
                 home_phone=None, mobile_phone=None, work_phone=None, secondary_phone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3

    def __repr__(self):
        return "%s %s: %s" % (self.first_name, self.last_name, self.id)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and\
               self.first_name == other.first_name and self.last_name == other.last_name


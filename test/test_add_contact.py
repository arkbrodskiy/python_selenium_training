from model.contact import Contact
import random
import string
import pytest




def get_random_name():
    return '%s%s' % (get_random_string_upper(1), get_random_string_lower(3, 15))


def get_random_email():
    return '%s@%s.%s' % (get_random_string_lower(2, 10), get_random_string_lower(3, 8), get_random_string_lower(2, 4))


def get_random_address():
    return '%s %s St., %stown, %s %s' % (get_random_string_digits(2, 5),
                                         (get_random_string_upper(1) + get_random_string_lower(3, 10)),
                                         (get_random_string_upper(1) + get_random_string_lower(3, 10)),
                                         get_random_string_upper(2), get_random_string_digits(5, 6))


def get_random_string_lower(min_len, max_len):
    return "".join([random.choice(string.ascii_lowercase) for i in range(random.randrange(min_len, max_len))])


def get_random_string_upper(len):
    return "".join([random.choice(string.ascii_uppercase) for i in range(len)])


def get_random_string_digits(min_len, max_len):
    return "".join([random.choice(string.digits) for i in range(random.randrange(min_len, max_len))])


test_data = [Contact(first_name=get_random_name(), last_name=get_random_name(), address=get_random_address(),
                     home_phone=get_random_string_digits(10, 11), work_phone=get_random_string_digits(10, 11),
                     mobile_phone=get_random_string_digits(10, 11), secondary_phone=get_random_string_digits(10, 11),
                     email=get_random_email(), email2=get_random_email(), email3=get_random_email()),
             Contact(first_name="", last_name="", address="", home_phone="", work_phone="",
                     mobile_phone="", secondary_phone="",
                     email="", email2="", email3="")]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.utils.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=app.utils.id_or_max) == sorted(new_contacts, key=app.utils.id_or_max)


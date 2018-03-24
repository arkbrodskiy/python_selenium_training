from random import randrange

from model.contact import Contact


def test_delete_some_contact(app):
    if app.group.count() == 0:
        app.contact.create(Contact(first_name='Created_first_name', last_name='Just_created_last_name'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.utils.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts


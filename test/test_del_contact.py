import random

from model.contact import Contact


def test_delete_some_contact(app, orm, check_ui):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_one_contact()
    old_contacts = orm.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = orm.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=app.utils.id_or_max) == sorted(new_contacts, key=app.utils.id_or_max)
    if check_ui:
        print('UI verification activated')
        assert sorted(new_contacts, key=app.utils.id_or_max) == \
            sorted(app.contact.get_contact_list(), key=app.utils.id_or_max)


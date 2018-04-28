import random

from model.contact import Contact


def test_modify_some_contact(app, db, check_ui):
    app.contact.ensure_contact_exists(db)
    old_contacts = db.get_contact_list()
    new_contact = Contact(first_name="Edited_first_name", last_name="Edited_last_name")
    contact_to_modify = random.choice(old_contacts)
    new_contact.id = contact_to_modify.id
    if new_contact.first_name is None:
        new_contact.first_name = contact_to_modify.first_name
    if new_contact.last_name is None:
        new_contact.last_name = contact_to_modify.last_name
    app.contact.modify_contact_by_id(new_contact)
    new_contacts = app.contact.get_contact_list()
    old_contacts.remove(contact_to_modify)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=app.utils.id_or_max) == sorted(new_contacts, key=app.utils.id_or_max)
    if check_ui:
        print('UI verification activated')
        assert sorted(new_contacts, key=app.utils.id_or_max) == \
            sorted(app.contact.get_contact_list(), key=app.utils.id_or_max)


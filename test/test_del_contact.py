import random

from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name='Created_first_name', last_name='Just_created_last_name'))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=app.utils.id_or_max) == sorted(new_contacts, key=app.utils.id_or_max)
    if check_ui:
        print('UI verification activated')
        assert sorted(new_contacts, key=app.utils.id_or_max) == \
            sorted(app.contact.get_contact_list(), key=app.utils.id_or_max)


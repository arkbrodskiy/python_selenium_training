from random import randrange

from model.contact import Contact


def test_modify_some_contact(app):
    app.contact.ensure_contact_exists(app)
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Edited_first_name", last_name="Edited_last_name")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    if contact.first_name is None:
        contact.first_name = old_contacts[index].first_name
    if contact.last_name is None:
        contact.last_name = old_contacts[index].last_name
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.utils.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=app.utils.id_or_max) == sorted(new_contacts, key=app.utils.id_or_max)


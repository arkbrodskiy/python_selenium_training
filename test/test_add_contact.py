from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="First_name", last_name="Last_name")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.utils.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=app.utils.id_or_max) ==sorted(new_contacts, key=app.utils.id_or_max)

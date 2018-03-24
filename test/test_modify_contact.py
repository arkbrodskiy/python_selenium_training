from model.contact import Contact


def test_modify_first_contact(app):
    if app.group.count() == 0:
        app.contact.create(Contact(first_name='Created_first_name', last_name='Just_created_last_name'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Edited_first_name", last_name="Edited_last_name")
    contact.id = old_contacts[0].id
    if contact.first_name is None:
        contact.first_name = old_contacts[0].first_name
    if contact.last_name is None:
        contact.last_name = old_contacts[0].last_name
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=app.utils.id_or_max) == sorted(new_contacts, key=app.utils.id_or_max)


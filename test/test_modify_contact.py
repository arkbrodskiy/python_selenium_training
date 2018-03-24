from model.contact import Contact


def test_modify_first_contact(app):
    if app.group.count() == 0:
        app.contact.create(Contact(first_name='Created_first_name', last_name='Just_created_last_name'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact("Edited_first_name", "Edited_last_name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


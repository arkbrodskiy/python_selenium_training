from model.contact import Contact


def test_modify_first_contact(app):
    if app.group.count() == 0:
        app.contact.create(Contact(first_name='Created_first_name', last_name='Just_created_last_name'))
    app.contact.modify_first_contact(Contact("Edited_first_name", "Edited_last_name"))

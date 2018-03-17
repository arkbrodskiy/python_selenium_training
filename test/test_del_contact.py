from model.contact import Contact


def test_delete_first_contact(app):
    if app.group.count() == 0:
        app.contact.create(Contact(first_name='Created_first_name', last_name='Just_created_last_name'))
    app.contact.delete_first_contact()

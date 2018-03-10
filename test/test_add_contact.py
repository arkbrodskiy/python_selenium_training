from model.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("First_name", "Last_name"))
    app.session.logout()


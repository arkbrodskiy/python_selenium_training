

def test_add_contact(app, orm, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = orm.get_contact_list()
    app.contact.create(contact)
    new_contacts = orm.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=app.utils.id_or_max) == sorted(new_contacts, key=app.utils.id_or_max)
    if check_ui:
        print('UI verification activated')
        assert sorted(new_contacts, key=app.utils.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=app.utils.id_or_max)

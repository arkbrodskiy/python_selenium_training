

def test_verify_all_contacts_on_home_page(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_one_contact()
    contacts_ui = sorted(app.contact.get_contact_list(), key=app.utils.id_or_max)
    contacts_db = sorted(orm.get_contact_list(), key=app.utils.id_or_max)
    assert len(contacts_ui) == len(contacts_db)
    for i in range(len(contacts_ui)):
        assert contacts_ui[i].first_name == contacts_db[i].first_name
        assert contacts_ui[i].last_name == contacts_db[i].last_name
        assert contacts_ui[i].address == contacts_db[i].address
        assert contacts_ui[i].all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contacts_db[i])
        assert contacts_ui[i].all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contacts_db[i])

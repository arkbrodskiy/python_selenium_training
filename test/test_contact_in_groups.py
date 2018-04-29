import random


def test_add_contact_to_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create_one_group()
    group = random.choice(orm.get_group_list())
    cl = orm.get_contacts_not_in_groups(group)
    if len(orm.get_contacts_not_in_groups(group)) == 0:
        app.contact.create_one_contact()
    contact = random.choice(orm.get_contacts_not_in_group(group))
    app.contact.add_to_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_groups(group)

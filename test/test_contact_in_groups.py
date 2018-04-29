import random


def test_add_contact_to_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create_one_group()
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_not_in_groups(group)) == 0:
        app.contact.create_one_contact()
    contact = random.choice(orm.get_contacts_not_in_groups(group))
    app.contact.add_to_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_groups(group)


def test_remove_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create_one_group()
    group = random.choice(orm.get_group_list())
    if len(orm.get_contact_list()) == 0:
        app.contact.create_one_contact()
    if len(orm.get_contacts_in_groups(group)) == 0:
        contact = random.choice(orm.get_contact_list())
        app.contact.add_to_group(contact.id, group.id)
    else:
        contact = random.choice(orm.get_contacts_in_groups(group))
    app.contact.remove_from_group(contact.id, group.id)
    assert contact in orm.get_contacts_not_in_groups(group)

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="Python group 01", header="p header 01", footer="p footer 01"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

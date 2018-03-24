from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="Python group 01", header="p header 01", footer="p footer 01")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=app.group.id_or_max) == sorted(new_groups)


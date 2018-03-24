from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="Python group 01", header="p header 01", footer="p footer 01")
    app.group.create(group)
    assert len(old_groups) + 1 == app.utils.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=app.utils.id_or_max) == sorted(new_groups, key=app.utils.id_or_max)


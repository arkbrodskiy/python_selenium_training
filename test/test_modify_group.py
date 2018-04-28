import random

from model.group import Group


def test_modify_some_group(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.create_one_group()
    old_groups = orm.get_group_list()
    new_group = Group(header="Super Edited group header", footer="Super Edited group footer")
    group_to_modify = random.choice(old_groups)
    new_group.id = group_to_modify.id
    if new_group.name is None:
        new_group.name = group_to_modify.name
    app.group.modify_group_by_id(new_group)
    new_groups = orm.get_group_list()
    old_groups.remove(group_to_modify)
    old_groups.append(new_group)
    assert sorted(old_groups, key=app.utils.id_or_max) == sorted(new_groups, key=app.utils.id_or_max)
    if check_ui:
        print('UI verification activated')
        assert sorted(new_groups, key=app.utils.id_or_max) == sorted(app.group.get_group_list(), key=app.utils.id_or_max)


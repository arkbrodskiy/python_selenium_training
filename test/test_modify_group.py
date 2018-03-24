from random import randrange

from model.group import Group


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Created_group_name', header='Just_created_header', footer='Fresh_footer'))
    old_groups = app.group.get_group_list()
    group = Group(header="Super Edited group header", footer="Super Edited group footer")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    if group.name is None:
        group.name = old_groups[index].name
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.utils.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=app.utils.id_or_max) == sorted(new_groups, key=app.utils.id_or_max)


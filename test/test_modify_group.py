import random
from random import randrange

from model.group import Group


def test_modify_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Created_group_name', header='Just_created_header', footer='Fresh_footer'))
    old_groups = db.get_group_list()
    new_group = Group(header="Super Edited group header", footer="Super Edited group footer")
    group_to_modify = random.choice(old_groups)
    new_group.id = group_to_modify.id
    if new_group.name is None:
        new_group.name = group_to_modify.name
    app.group.modify_group_by_id(new_group)
    new_groups = db.get_group_list()
    old_groups.remove(group_to_modify)
    old_groups.append(new_group)
    assert sorted(old_groups, key=app.utils.id_or_max) == sorted(new_groups, key=app.utils.id_or_max)


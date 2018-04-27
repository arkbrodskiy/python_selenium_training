from random import randrange
from model.group import Group
import random


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Created_group_name', header='Just_created_header', footer='Fresh_footer'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.utils.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups


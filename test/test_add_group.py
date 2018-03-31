import random
import string
from model.group import Group
import pytest


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


test_data = [Group(name=random_string('name', 10),
                   header=random_string('header', 20),
                   footer=random_string('footer', 20)),
             Group(name="", header="", footer="")]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.utils.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=app.utils.id_or_max) == sorted(new_groups, key=app.utils.id_or_max)


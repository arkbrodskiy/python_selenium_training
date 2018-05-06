import pytest


def test_add_group(app, orm, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = orm.get_group_list()
    with pytest.allure.step('When I add the group %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = orm.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=app.utils.id_or_max) == sorted(new_groups, key=app.utils.id_or_max)
        if check_ui:
            print('UI verification activated')
            assert sorted(new_groups, key=app.utils.id_or_max) == \
                sorted(app.group.get_group_list(), key=app.utils.id_or_max)


from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Created_group_name', header='Just_created_header', footer='Fresh_footer'))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(
        # name="Edited group name",
        header="Super Edited group header",
        # footer="Edited group footer"
        ))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

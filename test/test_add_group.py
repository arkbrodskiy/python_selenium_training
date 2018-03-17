from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Python group 01", header="p header 01", footer="p footer 01"))

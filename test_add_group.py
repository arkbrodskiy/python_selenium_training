# -*- coding: utf-8 -*-
from application import Application
import pytest
from group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Python group 01", header="p header 01", footer="p footer 01"))
    app.logout()

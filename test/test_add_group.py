# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="Python group 01", header="p header 01", footer="p footer 01"))
    app.session.logout()

# -*- coding: utf-8 -*-
import pytest
from model.kontakt import Kontakt
from fixture.application_2 import Application_2


@pytest.fixture
def app(request):
    fixture = Application_2()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_kontakt(app):
    app.session_2.login(username="admin", password="secret")
    app.group_2.fill_new_kontakt(Kontakt(first="qwer", middle="asdf", last="zxcv", phone="1234"))
    app.session_2.logout()

def test_add_empty_kontakt(app):
    app.session_2.login(username="admin", password="secret")
    app.group_2.fill_new_kontakt(Kontakt(first="", middle="", last="", phone=""))
    app.session_2.logout()




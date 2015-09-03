# -*- coding: utf-8 -*-
from model.kontakt import Kontakt


def test_add_kontakt(app):
    app.session_2.login(username="admin", password="secret")
    app.group_2.fill_new_kontakt(Kontakt(first="qwer", middle="asdf", last="zxcv", phone="1234"))
    app.session_2.logout()

def test_add_empty_kontakt(app):
    app.session_2.login(username="admin", password="secret")
    app.group_2.fill_new_kontakt(Kontakt(first="", middle="", last="", phone=""))
    app.session_2.logout()




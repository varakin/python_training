# -*- coding: utf-8 -*-
from model.kontakt import Kontakt


def test_add_kontakt(app):
    app.group.fill_new_kontakt(Kontakt(first="qwer", middle="asdf", last="zxcv", phone="1234"))


def test_add_empty_kontakt(app):
    app.group.fill_new_kontakt(Kontakt(first="", middle="", last="", phone=""))




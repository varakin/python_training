__author__ = 'varakin'

from model.group import Group



def test_mofify_group_name(app):
    app.group.modify_first_group(Group(name="New group"))

def test_mofify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))

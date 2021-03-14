from flask import current_app
from flask_appbuilder import AppBuilder, SQLA

app = current_app
db = SQLA()
appbuilder = AppBuilder()
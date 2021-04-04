from flask import current_app
from flask_appbuilder import AppBuilder, SQLA
from werkzeug.local import LocalProxy
from .jenkins_handler import JenkinsHandler
from .dsm_handler import DsmHandler

app = current_app
config = LocalProxy(lambda: app.config)
db = SQLA()
appbuilder = AppBuilder()
dsm_handler = DsmHandler()
jenkins_handler = JenkinsHandler()


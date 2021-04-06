from flask import current_app
from flask_appbuilder import AppBuilder, SQLA
from .jenkins_handler import JenkinsHandler
from .dsm_handler import DsmHandler


db = SQLA()
appbuilder = AppBuilder()
dsm_handler = DsmHandler()
jenkins_handler = JenkinsHandler()


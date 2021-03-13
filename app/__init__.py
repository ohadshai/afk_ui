import os

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from elasticapm.contrib.flask import ElasticAPM

from log import configure_logger
from .security import MySecurityManager
from app.index import  MyIndexView

from .jenkins_handler import JenkinsHandler


def load_config(app):
    env = os.environ.get('FLASK_ENV', 'production')
    config_type = ''.join(['config.', env.capitalize(), 'Config'])
    app.config.from_object(config_type)


app = Flask(__name__)
load_config(app)
apm = ElasticAPM(app)
configure_logger(app, apm)

# try:
#     1 / 0
# except ZeroDivisionError:
#     app.logger.error('I cannot math', exc_info=True)
    # logging.getLogger().error('I cannot math', exc_info=True)
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, base_template='baselayout.html', indexview=MyIndexView, security_manager_class=MySecurityManager)


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from . import views, models
from .devices.api import DevicesApi
from .jobs.api import JobsApi


appbuilder.add_api(DevicesApi)
appbuilder.add_api(JobsApi)

jenkins_handler = JenkinsHandler()
if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
    jobs_info = jenkins_handler.get_jobs_info()
    for jobs_info in jobs_info:
        job_type = models.JobType(name=jobs_info['name'].lstrip('afk_'), test_params=None, results_params=None)
        db.session.add(job_type)
        db.session.commit()





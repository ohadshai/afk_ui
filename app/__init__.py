import os
import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.handlers.logging import LoggingHandler

from log import configure_logger

"""
 Logging configuration
"""

# logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
# logging.getLogger().setLevel(logging.DEBUG)


def load_config():
    env = os.environ.get('FLASK_ENV', 'production')
    config_type = ''.join(['config.', env.capitalize(), 'Config'])
    app.config.from_object(config_type)
    configure_logger(app)


app = Flask(__name__)

load_config()
apm = ElasticAPM(app, logging=logging.ERROR)
# apm.capture_message('hello, world!')
# logging.getLogger().info("HELLLLO")
handler = LoggingHandler(client=apm.client)
handler.setLevel(logging.WARN)
app.logger.addHandler(handler)
try:
    1 / 0
except ZeroDivisionError:
    app.logger.error( 'I cannot math', exc_info=True)
db = SQLA(app)
appbuilder = AppBuilder(app, db.session)


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

from . import views
from .devices.api import DevicesApi
from .jobs.api import JobsApi

appbuilder.add_api(DevicesApi)
appbuilder.add_api(JobsApi)

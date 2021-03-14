import os
import logging
from logging.config import fileConfig
from elasticapm.handlers.logging import LoggingHandler


def configure_logger(app, apm):
    # Get logging config from file
    extra = {'env': os.environ.get('FLASK_ENV', 'production')}
    logging.config.fileConfig('logging.ini', defaults=extra)
    # adding hardcoded handler to apm
    handler = LoggingHandler(client=apm.client)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    # adding 'env' attribute to log msg
    app.logger = logging.LoggerAdapter(app.logger, extra)
    # disable 'werkzeug' logger
    logging.getLogger('werkzeug').disabled = True
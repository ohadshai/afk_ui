import os
import logging
from logging.config import fileConfig
from elasticapm.handlers.logging import LoggingHandler


def configure_logger(app, apm):
    handler = LoggingHandler(client=apm.client)
    # handler.setLevel(logging.WARN)
    app.logger.addHandler(handler)
    extra = {'env': os.environ.get('FLASK_ENV', 'production')}
    logging.config.fileConfig('logging.ini', defaults=extra, disable_existing_loggers=False)
    app.logger = logging.LoggerAdapter(app.logger, extra)
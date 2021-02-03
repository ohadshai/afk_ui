import os
import logging
from logging.config import fileConfig
from elasticapm.handlers.logging import LoggingHandler


def configure_logger(app, apm):
    extra = {'env': os.environ.get('FLASK_ENV', 'production')}
    logging.config.fileConfig('logging.ini', defaults=extra)

    handler = LoggingHandler(client=apm.client)
    handler.setLevel(logging.ERROR)
    # logging.root.addHandler(handler)
    app.logger.addHandler(handler)

    # logging.root = logging.LoggerAdapter(logging.root, extra)
    app.logger = logging.LoggerAdapter(app.logger, extra)
    logging.getLogger('werkzeug').disabled = True
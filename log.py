import os
import logging
from logging.config import fileConfig


def configure_logger(app):
    extra = {'env': os.environ.get('FLASK_ENV', 'production')}
    logging.LoggerAdapter(app.logger, extra)
    logging.config.fileConfig('logging.ini', defaults=extra)
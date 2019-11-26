import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

    @classmethod
    def init_app(cls, app):
        # DEBUG -> stdout
        stdh = logging.StreamHandler(sys.stdout)
        stdh.setLevel(logging.DEBUG)
        stdh_fmt = logging.Formatter('%(name)s:%(levelname)s:%(message)s')
        stdh.setFormatter(stdh_fmt)

        app.logger.addHandler(stdh)
        return app


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        # INFO -> stdout
        stdh = logging.StreamHandler(sys.stdout)
        stdh.setLevel(logging.INFO)
        stdh_fmt = logging.Formatter('%(name)s:%(levelname)s:%(message)s')
        stdh.setFormatter(stdh_fmt)

        # WARNING -> log file
        if not os.path.isdir('log'):
            os.mkdir('log')

        fh = TimedRotatingFileHandler(
            'log/warning.log',
            when='midnight',
            interval=1,
            backupCount=3,
            encoding='utf-8',
        )
        fh.setLevel(logging.WARNING)
        fh_fmt = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        fh.setFormatter(fh_fmt)

        app.logger.addHandler(stdh)
        app.logger.addHandler(fh)

        return app


configs = {
    'development': DevelopmentConfig,
    'test': TestingConfig,
    'production': ProductionConfig,
}

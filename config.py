import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = 'smtp.live.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = '[SUPERCHILLI]'
    MAIL_SENDER = 'Superchilli Admin<somelovebg@hotmail.com>'
    ADMAIN = os.environ.get('ADMAIN')
    POSTS_PER_PAGE = 20
    FOLLOWERS_PER_PAGE = 50
    COMMENTS_PER_PAGE = 30
    SLOW_DB_QUERY_TIME = 0.5
    UPLOAD_FOLDER_ROOT = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER_PATH = 'app/static/uploads'
    UPLOAD_FOLDER = os.path.join(UPLOAD_FOLDER_ROOT, UPLOAD_FOLDER_PATH)


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'prodution': ProductionConfig,

    'default': DevelopmentConfig
}




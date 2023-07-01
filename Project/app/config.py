import os
class Config(object):
    app_dir = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%storage.db' % app_dir

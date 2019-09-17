import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'

    MAIL_USERNAME = '<gmail>'
    MAIL_PASSWORD = '<password>'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True

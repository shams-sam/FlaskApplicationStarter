import os

class Config:
    APP_NAME = "ICD Demo Application"
    SECRET_KEY = os.environ['SECRET_KEY']
    WTF_CSRF_ENABLED = os.environ['WTF_CSRF_ENABLED'] == 'True'
    DEBUG = os.environ['DEBUG'] == 'True'

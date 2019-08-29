import os


class Config:
    SECRET_KEY = 'b0e8006aa0d9e8f7535a6867bac293fa'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp@gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # app.config['MAIL_USE_SSL'] = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
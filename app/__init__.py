from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import (basedir,
                    ADMINS,
                    MAIL_SERVER,
                    MAIL_PORT,
                    MAIL_USERNAME,
                    MAIL_PASSWORD)
import os

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# login with OpenID
lm = LoginManager()
lm.init_app(app)
#Flask-Login needs to know what view logs users in
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

# import views to work
from app import views

# when error we send out a email
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT),
                               'no-reply@' + MAIL_SERVER,
                               ADMINS,
                               'microblog failure')
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

# we log INFO in tmp/microblog.log
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')

#!/usr/bin/env python
from app import app, db
from app.models import User, Post
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand


db.create_all()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

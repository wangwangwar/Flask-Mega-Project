#!/usr/bin/env python
from app import app, db

db.create_all()

if __name__ == '__main__':
    app.run(debug=False)

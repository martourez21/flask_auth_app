from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import db


class Users(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __repr__(self):
        return f'<Users {self.id} {self.email}>'

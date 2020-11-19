# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash

from todolist import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username')
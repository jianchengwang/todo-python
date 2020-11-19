# -*- coding: utf-8 -*-
from flask import request, Response, url_for, jsonify
import json
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity
)
from todolist import utils
from .model import User
from todolist import app, jwt

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
        return utils.falseReturn(message= 'Invalid input.')

    user = User.query.first()
    if username == user.username and user.validate_password(password):
        access_token = create_access_token(identity=username)
        return utils.trueReturn(data = access_token, message= 'Login success.')

    return utils.falseReturn(message= 'Invalid username or password.')

@app.route('/logout')
def logout():
    return utils.trueReturn(data = '' ,message= 'Logout success.')
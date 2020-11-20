# -*- coding: utf-8 -*-
from flask import request, Response, url_for, jsonify
import json
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from todolist import app, db, utils
from .model import User, UserSchema

user_schema = UserSchema()

@app.route('/currentUser')
@jwt_required
def currentUser():
    current_user_name = get_jwt_identity()
    current_user = User.query.filter_by(username=current_user_name).first()
    if(current_user):
        return utils.result(data=user_schema.dump(current_user))
    return utils.notFound()


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
        return utils.badRequest(msg= 'Invalid input.')

    user = User(username=request.form['username'])
    user.set_password(request.form['password'])
    db.session.add(user)
    db.session.commit()
    return utils.result(msg= 'Register successed.')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
        return utils.badRequest(msg= 'Invalid input.')

    user = User.query.first()
    if username == user.username and user.validate_password(password):
        access_token = create_access_token(identity=username)
        return utils.result(data = access_token)

    return utils.badRequest(msg= 'Invalid username or password.')

@app.route('/logout')
def logout():
    return utils.result()
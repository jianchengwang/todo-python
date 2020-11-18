# -*- coding: utf-8 -*-
from flask import request, Response, url_for, jsonify
from flask_login import login_user, login_required, logout_user, current_user
import json

from todolist import app, db, ma
from todolist.models import User, UserSchema, TodoItem, TodoItemSchema

@app.route('/todoItems', methods=['GET'])
def all():
    todoItems = TodoItem.query.all()
    todoitems_schema = TodoItemSchema(many=True)
    return Response(json.dumps(todoitems_schema.dump(todoItems),  mimetype='application/json')

@app.route('/todoItem/edit/<int:item_id>', methods=['POST'])
@login_required
def edit(item_id):
    todoItem = TodoItem.query.get_or_404(item_id)
    title = request.form['title']
    descs = request.form['descs']

    if not title or len(title) > 60:
        return {
            "code": -1,
            "message": 'Invide title'
        }
    todoItem.title = title
    todoItem.descs = descs
    db.session.commit()
    return {
        "code": 0,
        "message": 'Item updated.'
    }

@app.route('/todoItem/delete/<int:item_id>', methods=['POST'])
@login_required
def delete(item_id):
    todoItem = TodoItem.query.get_or_404(item_id)
    db.session.delete(todoItem)
    db.session.commit()
    return {
        "code": 0,
        "message": 'Item deleted.'
    }


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
        return {
            "code": -1,
            "message": 'Invalid input.'
        }

    user = User.query.first()
    if username == user.username and user.validate_password(password):
        login_user(user)
        return {
            "code": 0,
            "message": 'Login success.'
        }

    return {
        "code": -1,
        "message": 'Invalid username or password.'
    }

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return {
        "code": 0,
        "message": 'Goodbye.'
    }
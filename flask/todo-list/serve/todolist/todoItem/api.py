# -*- coding: utf-8 -*-
import sys
from flask import request, Response, url_for, jsonify
import json
from flask_jwt_extended import jwt_required, get_jwt_identity
from todolist import app, db, utils
from .model import TodoItem, TodoItemSchema

todoitem_schema = TodoItemSchema()

@app.route('/todoItem', methods=['GET'])
@jwt_required
def all():
    todoItems = TodoItem.query.all()
    return utils.result(data=todoitem_schema.dump(todoItems, many=True))

@app.route('/todoItem/<int:item_id>', methods=['GET'])
@jwt_required
def get(item_id):
    todoItem = TodoItem.query.get_or_404(item_id)
    return utils.result(data=todoitem_schema.dumps(todoItem))

@app.route('/todoItem', methods=['POST'])
@jwt_required
def add():
    todoItem = TodoItem(title = request.form['title'], descs = request.form['descs'])
    db.session.add(todoItem)
    db.session.commit()
    return utils.result(msg= 'Item added.')

@app.route('/todoItem/<int:item_id>', methods=['PUT'])
@jwt_required
def update(item_id):
    todoItem = TodoItem.query.get_or_404(item_id)
    title = request.form['title']
    descs = request.form['descs']

    if not title or len(title) > 60:
        return utils.badRequest(msg= 'Invide title.')
    todoItem.title = title
    todoItem.descs = descs
    db.session.commit()
    return utils.result(msg= 'Item updated.')

@app.route('/todoItem/<int:item_id>', methods=['DELETE'])
@jwt_required
def delete(item_id):
    todoItem = TodoItem.query.get_or_404(item_id)
    db.session.delete(todoItem)
    db.session.commit()
    return utils.result(msg= 'Item deleted.')

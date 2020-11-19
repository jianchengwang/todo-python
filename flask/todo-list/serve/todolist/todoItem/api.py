# -*- coding: utf-8 -*-
from flask import request, Response, url_for, jsonify
import json
from flask_jwt_extended import jwt_required, get_jwt_identity
from todolist import app, db
from .model import TodoItem, TodoItemSchema

@app.route('/todoItem', methods=['GET'])
def all():
    todoItems = TodoItem.query.all()
    todoitem_schema = TodoItemSchema()
    return jsonify(todoitem_schema.dumps(todoItems, many=True))

@app.route('/todoItem/<int:item_id>', methods=['GET'])
def get(item_id):
    todoItem = TodoItem.query.get_or_404(item_id)
    todoitem_schema = TodoItemSchema()
    return jsonify(todoitem_schema.dumps(todoItem))

@app.route('/todoItem', methods=['POST'])
@jwt_required
def add():
    todoItem = TodoItem(title = request.form['title'], descs = request.form['descs'])
    db.session.add(todoItem)
    db.session.commit()
    return {
        "code": 0,
        "message": 'Item added.'
    }

@app.route('/todoItem/<int:item_id>', methods=['PUT'])
@jwt_required
def update(item_id):
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

@app.route('/todoItem/delete/<int:item_id>', methods=['DELETE'])
@jwt_required
def delete(item_id):
    todoItem = TodoItem.query.get_or_404(item_id)
    db.session.delete(todoItem)
    db.session.commit()
    return {
        "code": 0,
        "message": 'Item deleted.'
    }

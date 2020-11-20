# -*- coding: utf-8 -*-
import click

from . import app, db
from .todoItem.model import TodoItem
from .user.model import User


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    username = 'wjc'
    todoItems = [
        {'title': 'flask', 'descs': 'learn flask'},
        {'title': 'vue', 'descs': 'learn vue'},
        {'title': 'node.js', 'descs': 'learn node.js'},
        {'title': 'linux', 'descs': 'learn linux'}
    ]

    user = User(username=username)
    db.session.add(user)
    for item in todoItems:
        todoItem = TodoItem(title=item['title'], descs=item['descs'])
        db.session.add(todoItem)

    db.session.commit()
    click.echo('Done.')


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)
    else:
        click.echo('Creating user...')
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('Done.')
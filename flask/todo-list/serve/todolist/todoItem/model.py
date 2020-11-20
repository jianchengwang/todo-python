from todolist import db, ma

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    descs = db.Column(db.String(256))

class TodoItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TodoItem
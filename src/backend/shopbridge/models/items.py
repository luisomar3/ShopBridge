from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from shopbridge import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, description, price, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def json(self):
        return {'id': self.id, 'name': self.name, 'description': self.description,
                'price': self.price, 'quantity': self.quantity, 'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')}

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, item_id):
        return cls.query.filter_by(id=item_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

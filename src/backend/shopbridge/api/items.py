from flask import Blueprint, jsonify, request
from shopbridge.models.items import Item
from shopbridge import db

items_bp = Blueprint('items_bp', __name__, url_prefix='/api/items')

@items_bp.route('/', methods=['POST'])
async def create_item():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    if not name or not description or not price:
        return jsonify({'error': 'Name, description, and price are required.'}), 400
    item = Item(name=name, description=description, price=price)
    db.session.add(item)
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price}), 201

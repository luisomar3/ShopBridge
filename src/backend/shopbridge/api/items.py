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

@items_bp.route('/<int:item_id>', methods=['PUT'])
async def update_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'error': f'Item with id {item_id} not found.'}), 404
    data = request.json
    name = data.get('name', item.name)
    description = data.get('description', item.description)
    price = data.get('price', item.price)
    item.name = name
    item.description = description
    item.price = price
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price})

@items_bp.route('/<int:item_id>', methods=['DELETE'])
async def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'error': f'Item with id {item_id} not found.'}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': f'Item with id {item_id} deleted.'})

@items_bp.route('/', methods=['GET'])
async def list_items():    
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price} for item in items])

@items_bp.route('/<int:id>', methods=['GET'])
async def get_item(id):
    item = Item.query.get(id)
    if item:
        return jsonify({'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price})
    else:
        return jsonify({'error': 'Item not found'})
    
@items_bp.route('/bulk', methods=['POST'])
async def bulk_insert_items():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided.'}), 400
    if not isinstance(data, list):
        return jsonify({'error': 'Data must be a list.'}), 400
    items = []
    for item_data in data:
        name = item_data.get('name')
        description = item_data.get('description')
        price = item_data.get('price')
        if not name or not description or not price:
            return jsonify({'error': 'Name, description, and price are required for all items.'}), 400
        item = Item(name=name, description=description, price=price)
        items.append(item)
    db.session.bulk_save_objects(items)
    db.session.commit()
    return jsonify({'message': f'{len(items)} items inserted.'})
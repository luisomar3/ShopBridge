from flask import Blueprint, jsonify, request,Response
from flask_jwt_extended import jwt_required, get_jwt_identity

from shopbridge.models.items import Item
from shopbridge import db
from shopbridge.utils.exception_handler import handle_exceptions

items_bp = Blueprint('items_bp', __name__, url_prefix='/api/items')


@items_bp.route('/')
@handle_exceptions
@jwt_required()
async def create_item():
    print(request)
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'error': 'User not authenticated.'}), 401
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
@handle_exceptions
@jwt_required()
async def update_item(item_id):
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'error': 'User not authenticated.'}), 401
    
    item = db.session.get(Item,item_id)
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
@handle_exceptions
@jwt_required()
async def delete_item(item_id):
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'error': 'User not authenticated.'}), 401
    
    item = db.session.get(Item,item_id)
    if not item:
        return jsonify({'error': f'Item with id {item_id} not found.'}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': f'Item with id {item_id} deleted.'})

@items_bp.route('/', methods=['GET'])
@handle_exceptions
@jwt_required()
async def list_items():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'error': 'User not authenticated.'}), 401    
    items = db.session.query(Item).all()
    return jsonify([{'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price} for item in items])

@items_bp.route('/<int:item_id>', methods=['GET'])
@handle_exceptions
@jwt_required()
async def get_item(item_id):
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'error': 'User not authenticated.'}), 401
    item = db.session.get(Item,item_id)
    if item:
        return jsonify({'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price})
    else:
        return jsonify({'error': 'Item not found'}),404
    
@items_bp.route('/bulk', methods=['POST'])
@handle_exceptions
@jwt_required()
async def bulk_insert_items():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'error': 'User not authenticated.'}), 401
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
    return jsonify({'message': f'{len(items)} items inserted.'}),201

@handle_exceptions
@items_bp.route("/ping",methods=['GET'])
def health():
    return Response("OK", status=200)
from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from shopbridge.models.user import User
from shopbridge.utils.auth import generate_jwt_tokens, authenticate_user
from shopbridge import db

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'User already exists.'}), 400
    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    access_token,access_token_expires,refresh_token,refresh_token_expire = generate_jwt_tokens(user)
    return jsonify(
        {'access_token': access_token, 
         'access_token_expires':access_token_expires,
         'refresh_token': refresh_token,
         'refresh_token_expire':refresh_token_expire
         }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400
    user = authenticate_user(email, password)
    if not user:
        return jsonify({'error': 'Invalid email or password.'}), 401
    access_token,access_token_expires,refresh_token,refresh_token_expire = generate_jwt_tokens(user)
    return jsonify(
        {'access_token': access_token, 
         'access_token_expires':access_token_expires,
         'refresh_token': refresh_token,
         'refresh_token_expire':refresh_token_expire
         }), 201

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    if not user:
        return jsonify({'error': 'User not found.'}), 400
    
    access_token,access_token_expires,refresh_token,refresh_token_expire = generate_jwt_tokens(user)
    return jsonify(
        {'access_token': access_token, 
         'access_token_expires':access_token_expires,
         'refresh_token': refresh_token,
         'refresh_token_expire':refresh_token_expire
         }), 201
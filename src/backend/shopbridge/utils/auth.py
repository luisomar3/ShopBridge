from datetime import datetime,timedelta
from flask_jwt_extended import create_access_token,create_refresh_token
from flask import current_app
from shopbridge.models.user import User

def generate_jwt_tokens(user):
    access_token_expiry_delta = timedelta(minutes=current_app.config.get('JWT_ACCESS_TOKEN_EXPIRY'))
    access_token_expiry_date = datetime.utcnow() + access_token_expiry_delta
    access_token = create_access_token(identity=user.id, expires_delta=access_token_expiry_delta)
    
    refresh_token_expiry = timedelta(days=current_app.config.get('JWT_REFRESH_TOKEN_EXPIRY'))
    refresh_token_expiry_date = datetime.utcnow() + refresh_token_expiry
    refresh_token = create_refresh_token(identity=user.id, expires_delta=refresh_token_expiry)
    
    return access_token,access_token_expiry_date,refresh_token,refresh_token_expiry_date

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return None
    return user

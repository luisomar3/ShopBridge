from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from shopbridge import db

class RevokedToken(db.Model):
    __tablename__ = 'revoked_tokens'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    type = db.Column(db.String(16), nullable=True)
    revoked_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, jti, user_id):
        self.jti = jti
        self.user_id = user_id

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
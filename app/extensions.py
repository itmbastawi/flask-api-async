# app/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask import redirect, url_for

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
jwt = JWTManager()



@jwt.unauthorized_loader
def unauthorized_callback(reason):
    return redirect(url_for(''))

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    print("JWT Payload:")
    # refresh token
    redirect_url = url_for('auth.refresh', _external=True)
    if 'next' in jwt_payload:
        redirect_url += f'?next={jwt_payload["next"]}'
    return redirect(redirect_url)
    
# app/services/auth.py
from ..extensions import db
from ..models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt
)
from datetime import datetime, timezone

class AuthService:
    @staticmethod
    async def authenticate_user(username: str, password: str):
        user = db.session.execute(
            db.select(User).filter_by(username=username)
        ).scalar_one_or_none()

        if user and check_password_hash(user.password_hash, password):
            # Create both access and refresh tokens
            access_token = create_access_token(
                identity=user.id,
                additional_claims={
                    "username": user.username
                }
            )
            refresh_token = create_refresh_token(
                identity=user.id,
                additional_claims={
                    "username": user.username
                }
            )
            
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user_id": user.id,
                "username": user.username
            }
        return None

    @staticmethod
    async def create_user(username: str, email: str, password: str):
        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        return user

# app/utils/auth.py
from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, get_jwt

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        async def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("is_admin"):
                return await fn(*args, **kwargs)
            else:
                return jsonify(message="Admins only!"), 403
        return decorator
    return wrapper
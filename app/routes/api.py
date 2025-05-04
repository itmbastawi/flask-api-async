# app/routes/api.py
from flask import Blueprint, jsonify
from ..utils.auth import admin_required
from flask_jwt_extended import jwt_required, get_jwt_identity

api_bp = Blueprint('api', __name__)

@api_bp.route('/protected', methods=['GET'])
@jwt_required()
async def protected():
    current_user_id = get_jwt_identity()
    return jsonify(logged_in_as=current_user_id), 200

@api_bp.route('/admin', methods=['GET'])
@admin_required()
async def admin():
    return jsonify(message="Welcome, Admin!"), 200
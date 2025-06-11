# app/routes/api.py
from flask import Blueprint, jsonify
from ..utils.auth import admin_required
from flask_jwt_extended import jwt_required, get_jwt_identity

api_bp = Blueprint('api', __name__)

@api_bp.route('/admin', methods=['GET'])
@admin_required()
async def admin():
    return jsonify(message="Welcome, Admin!"), 200
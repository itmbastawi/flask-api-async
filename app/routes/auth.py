# app/routes/auth.py
from flask import Blueprint, request, jsonify
from ..schemas.user import UserSchema, UserLoginSchema
from ..services.auth import AuthService
from marshmallow import ValidationError

auth_bp = Blueprint('auth', __name__)
user_schema = UserSchema()
user_login_schema = UserLoginSchema()

@auth_bp.route('/register', methods=['POST'])
async def register():
    try:
        # Validate and deserialize input
        user_data =  request.get_json()
        user =  user_schema.load(user_data)
        # Create user

        result = await  AuthService.create_user(user.username, user.email, user.password_hash)
    
        # Serialize and return response
        return jsonify({
            'status': 'success',
            'message': 'User created successfully',
            'data': user_schema.dump(result)
        }), 201
        
    except ValidationError as err:
        return jsonify({
            'status': 'error',
            'message': 'Validation error',
            'errors': err.messages
        }), 400

@auth_bp.route('/login', methods=['POST'])
async def login():

    data = request.get_json()
    
    try:
        # Validate and deserialize input
        login_data = user_login_schema.load({"username": data.get('username'),
                                             "password_hash": data.get('password')})
        
        # Authenticate user
        result = await AuthService.authenticate_user(
            login_data['username'],
            login_data['password_hash']
        )
        
        if not result:
            return jsonify({
                'status': 'error',
                'message': 'Invalid credentials'
            }), 401
            
        return jsonify({
            'status': 'success',
            'data': result
        })
        
    except ValidationError as err:
        return jsonify({
            'status': 'error',
            'message': 'Validation error',
            'errors': err.messages
        }), 400
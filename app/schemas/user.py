# app/schemas/user.py
from ..extensions import ma
from . import BaseSchema, Length, Email, ValidationError
from ..models.user import User
from marshmallow import post_load, pre_load, fields, validates

class UserSchema(BaseSchema):
    class Meta:
        model = User
        load_instance = True
        ordered = True  # Keep the order of fields in the output

    id = ma.auto_field(dump_only=True)
    username = fields.String(
        required=True,
        validate=[Length(min=3, max=80)],
        error_messages={"required": "Username is required"}
    )
    email = fields.Email(
        required=True,
        validate=[Email()],
        error_messages={"required": "Email is required"}
    )
    password_hash = fields.String(
        required=True,
        load_only=True,  # Password will only be used when loading data
        validate=[Length(min=6, max=128)],
        error_messages={
            "required": "Password is required",
            "validator_failed": "Password must be between 6 and 128 characters"
        }
    )
    created_at = fields.DateTime(dump_only=True)

    # Nested relationships (if any)
    # posts = fields.Nested('PostSchema', many=True, dump_only=True)

    @validates('username')
    def validate_username(self, value, **kwargs):
        if User.query.filter_by(username=value).first():
            raise ValidationError('Username already exists')

    @validates('email')
    def validate_email(self, value, **kwargs):
        if User.query.filter_by(email=value).first():
            raise ValidationError('Email already exists')

    @pre_load
    def process_input(self, data, **kwargs):
        """Clean input data before loading"""
        data = data or {}
        if 'username' in data:
            data['username'] = data['username'].lower().strip()
        if 'email' in data:
            data['email'] = data['email'].lower().strip()
        if 'password' in data:
            data['password_hash'] = data['password'].strip()
            del data['password']
        return data

class UserUpdateSchema(UserSchema):
    """Schema for updating user information"""
    password = fields.String(
        required=False,
        load_only=True,
        validate=[Length(min=6, max=128)]
    )

class UserLoginSchema(BaseSchema):
    """Schema for user login"""
    class Meta:
        model = User
        ordered = True
    username = fields.String(required=True)
    password_hash = fields.String(required=True, load_only=True)
    

    

class UserPublicSchema(BaseSchema):
    """Schema for public user information"""
    class Meta:
        model = User
        ordered = True

    id = ma.auto_field(dump_only=True)
    username = ma.auto_field(dump_only=True)
    created_at = ma.auto_field(dump_only=True)

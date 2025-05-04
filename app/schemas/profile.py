# app/schemas/profile.py
from ..extensions import ma
from . import BaseSchema, Length, ValidationError
from ..models.profile import Profile
from marshmallow import fields

class ProfileSchema(BaseSchema):
    class Meta:
        model = Profile
        load_instance = True
        ordered = True

    id = ma.auto_field(dump_only=True)
    bio = fields.String(validate=[Length(max=500)])
    location = fields.String(validate=[Length(max=100)])
    avatar_url = fields.URL()
    user_id = ma.auto_field(dump_only=True)
    
    # Nested user relationship
    user = fields.Nested('UserPublicSchema', dump_only=True)

    @validates('bio')
    def validate_bio(self, value):
        if value and len(value.strip()) < 10:
            raise ValidationError('Bio must be at least 10 characters long')
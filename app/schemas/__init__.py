# app/schemas/__init__.py
from ..extensions import ma
from marshmallow import validates, ValidationError, validates_schema
from marshmallow.validate import Length, Email, Range

# Base Schema with common functionality
class BaseSchema(ma.SQLAlchemySchema):
    class Meta:
        load_instance = True
    
    @validates_schema
    def validate_empty_strings(self, data, **kwargs):
        """Validate that string fields are not empty or just whitespace"""
        for field_name, value in data.items():
            if isinstance(value, str) and not value.strip():
                raise ValidationError(f"{field_name} cannot be empty or whitespace")
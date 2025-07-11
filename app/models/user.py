# app/models/user.py
from ..extensions import db
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash 

class User(db.Model):
    __tablename__ = 'users'  # Changed from 'user' to 'users' for consistency
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='user')
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    # Add relationship to groups through association table
    groups = db.relationship('Group', secondary='user_groups', back_populates='users')
    boats = db.relationship('Boat', backref='owner', lazy=True)
    profile = db.relationship('UserProfile', backref='user', uselist=False, cascade="all, delete-orphan")
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, index=True)
    description = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    # Add relationship to users through association table
    users = db.relationship('User', secondary='user_groups', back_populates='groups')

    def __repr__(self):
        return f'<Group {self.name}>'


class UserGroup(db.Model):
    __tablename__ = 'user_groups'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id', ondelete='CASCADE'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f'<UserGroup user_id={self.user_id} group_id={self.group_id}>'


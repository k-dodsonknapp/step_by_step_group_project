from app.models.db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey, Text, LargeBinary
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    userPhoto = Column(LargeBinary, nullable=True)
    photoType = Column(String(10), nullable=True)

    project = relationship('Project', back_populates='user')
    comments = relationship('Comment', back_populates='user')

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    

    def to_dict(self):
        import base64
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'userPhoto': (
                base64.b64encode(self.userPhoto).decode('utf-8') if isinstance(self.userPhoto, bytes)
                else self.userPhoto
            ),
            'photoType': self.photoType
        }

# Import models at the end to avoid circular dependencies
from .project import Project
from .comment import Comment

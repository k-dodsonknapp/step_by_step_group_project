from app.models.db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

class Project(db.Model):
    __tablename__ = 'projects'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    title = Column(String(100), nullable=False)
    titleImage = Column(Text, nullable=False)
    overview = Column(Text, nullable=False)
    category = Column(String(50), nullable=False)
    views = Column(Integer, default=0)
    favorites = Column(Integer, default=0)

    user = relationship('User', back_populates='project')
    instruction = relationship('Instruction', back_populates='project')
    supply = relationship('Supply', back_populates='project')
    comments = relationship('Comment', back_populates='project')


    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'title': self.title,
            'titleImage': self.titleImage,
            'overview': self.overview,
            'category': self.category,
            'views': self.views,
            'favorites': self.favorites,
        }

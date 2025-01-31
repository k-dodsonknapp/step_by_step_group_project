from app.models.db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

class Instruction(db.Model):
    __tablename__ = 'instructions'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    projectId = Column(Integer, ForeignKey(add_prefix_for_prod('projects.id')), nullable=False)
    stepOrder = Column(Integer, nullable=False)
    stepTitle = Column(String(100))
    instructions = Column(Text)
    photoUrl = Column(Text)
    videoUrl = Column(Text)

    project = relationship('Project', back_populates='instruction')


    def to_dict(self):
        return {
            'id': self.id,
            'projectId': self.projectId,
            'stepTitle': self.stepTitle,
            'stepOrder': self.stepOrder,
            'instructions': self.instructions,
            'photoUrl': self.photoUrl,
            'videoUrl': self.videoUrl
        }

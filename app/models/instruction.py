from .db import db

class Instruction(db.Model):
    __tablename__ = 'instructions'

    id = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    stepOrder = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    photoUrl = db.Column(db.Text)
    viedoUrl = db.Column(db.Text)

    project = db.relationship('Project', back_populates='instruction')

from app.models.db import db

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    projectId = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)

    user = db.relationship('User', back_populates='comment')
    project = db.relationship('Project', back_populates='comment')

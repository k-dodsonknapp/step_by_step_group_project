from app.models.db import db

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    titleImage = db.Column(db.Text, nullable=False)
    overview = db.Column(db.Text, nullable=False)
    categoryId = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    user = db.relationship('User', back_populates='project')
    instruction = db.relationship('Instruction', back_populates='project')
    supply = db.relationship('Supply', back_populates='project')
    comment = db.relationship('Coment', back_populates='project')
    category = db.relationship('Category', back_populates='project')
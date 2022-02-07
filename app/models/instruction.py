from app.models.db import db

class Instruction(db.Model):
    __tablename__ = 'instructions'

    id = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    stepOrder = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    photoUrl = db.Column(db.Text)
    viedoUrl = db.Column(db.Text)

    project = db.relationship('Project', back_populates='instruction')



    def to_dict(self):
        return {
            'id': self.id,
            'projectId': self.projectId,
            'stepOrder': self.stepOrder,
            'instructions': self.instructions,
            'photoUrl': self.photoUrl,
            'videoUrl': self.viedoUrl
        }

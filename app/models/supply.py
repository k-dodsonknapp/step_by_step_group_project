from app.models.db import db

class Supply(db.Model):
    __tablename__ = 'supplies'

    id = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    supply = db.Column(db.String(150), nullable=False)
    amount = db.Column(db.Integer)

    project = db.relationship('Project', back_populates='supply')


    def to_dict(self):
        return {
            'id': self.id,
            'projectId': self.projectId,
            'supply': self.supply,
            'amount': self.amount,
        }

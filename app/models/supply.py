from app.models.db import db, environment, SCHEMA, add_prefix_for_prod

class Supply(db.Model):
    __tablename__ = 'supplies'
    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('projects.id')), nullable=False)
    supply = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Integer)

    project = db.relationship('Project', back_populates='supply')


    def to_dict(self):
        return {
            'id': self.id,
            'projectId': self.projectId,
            'supply': self.supply,
            'amount': self.amount,
        }

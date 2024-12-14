from app.models.db import db, environment, SCHEMA, add_prefix_for_prod

class Comment(db.Model):
    __tablename__ = 'comments'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    projectId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('projects.id')), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False)

    user = db.relationship('User', back_populates='comments')
    project = db.relationship('Project', back_populates='comments')


    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'projectId': self.projectId,
            'comment': self.comment,
            'username': self.username,
        }
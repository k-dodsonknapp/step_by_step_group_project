# from app.models.db import db, environment, SCHEMA, add_prefix_for_prod

# class Views(db.Model):
#     __tablename__ = 'views'
#     if environment == "production":
#         __table_args__ = {'schema': SCHEMA}

#     id = db.Column(db.Integer, primary_key=True)
#     projectId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('projects.id')), nullable=False)
#     viewCount = db.Column(db.Integer, nullable=False)

#     project = db.relationship('Project', back_populates='views')

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'projectId': self.projectId,
#             'viewCount': self.viewCount,
#         }
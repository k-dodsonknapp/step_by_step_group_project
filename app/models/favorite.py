# from app.models.db import db, environment, SCHEMA, add_prefix_for_prod

# class Favorite(db.Model):
#     __tablename__ = "favorites"
#     if environment == "production":
#         __table_args__ = {'schema': SCHEMA}

#     id = db.Column(db.Integer, primary_key=True)
#     projectId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('projects.id')), nullable=False)
#     userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

#     user = db.relationship("User", back_populates='favorite')
#     project = db.relationship("Project", back_populates="favorite")

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "projectId": self.projectId,
#             "userId": self.userId,
#         }

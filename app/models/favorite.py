from app.models.db import db

class Favorite(db.Model):
    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship("User", back_populates='favorite')
    project = db.relationship("Project", back_populates="favorite")

    def to_dict(self):
        return {
            "id": self.id,
            "projectId": self.projectId,
            "userId": self.userId,
        }

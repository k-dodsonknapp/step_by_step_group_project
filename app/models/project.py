from app.models.db import db, environment, SCHEMA, add_prefix_for_prod

class Project(db.Model):
    __tablename__ = 'projects'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    titleImage = db.Column(db.Text, nullable=False)
    overview = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    user = db.relationship('User', back_populates='project')
    instruction = db.relationship('Instruction', back_populates='project')
    supply = db.relationship('Supply', back_populates='project')
    comment = db.relationship('Comment', back_populates='project')
    views = db.relationship('Views', back_populates='project')
    favorite = db.relationship("Favorite", back_populates="project")


    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'title': self.title,
            'titleImage': self.titleImage,
            'overview': self.overview,
            'category': self.category
        }

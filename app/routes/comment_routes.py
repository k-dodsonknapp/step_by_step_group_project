from flask import Blueprint, request
from app.models.db import db
from app.models.comment import Comment


comment_bp = Blueprint('comments', __name__)

@comment_bp.route('/new', methods=['POST'])
def create_comment():
    data = request.json

    comment = Comment(userId=data['userId'],
                      projectId=data['projectId'],
                      comment=data['comment'],
                      username=data['username'])

    db.session.add(comment)
    db.session.commit()

    return {'comment': comment.to_dict()}

@comment_bp.route('/<int:id>', methods=['DELETE'])
def delete_comment(id):

    comment = Comment.query.get(id)
    db.session.delete(comment)
    db.session.commit()

    return {'message': 'success'}

@comment_bp.route('/<int:id>', methods=['PUT'])
def edit_comment(id):
    data = request.json

    comment = Comment.query.get(id)
    comment.comment = data['comment']
    # db.session.add(comment)
    db.session.commit()

    return comment.to_dict()

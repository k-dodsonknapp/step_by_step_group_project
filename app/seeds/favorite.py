# from app.models import db, Favorite
# import os
# environment = os.getenv("FLASK_ENV")
# SCHEMA = os.environ.get("SCHEMA")

# def seed_favorites():
#     project1_favorite = Favorite(
#         projectId=1,
#         userId=1,
#     )

#     project_favorite2 = Favorite(
#         projectId=1,
#         userId=2,
#     )

#     db.session.add(project1_favorite)
#     db.session.add(project_favorite2)

#     db.session.commit()

# def undo_favorites():
#     if environment == "production":
#         db.session.execute(f"TRUNCATE table {SCHEMA}.favorites RESTART IDENTITY CASCADE;")
#     else:
#         db.session.execute("DELETE FROM favorites")

#     db.session.commit()
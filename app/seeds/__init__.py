from flask.cli import AppGroup
from app.seeds.favorite import seed_favorites, undo_favorites
from app.seeds.instruction_seeder import seed_instructions, undo_instructions
from app.seeds.supply_seeder import seed_supplies, undo_supplies
from app.seeds.comment_seeder import seed_comments, undo_comments

from app.seeds.projects_seeder import seed_project, undo_projects
from app.seeds.views_seeder import seed_views, undo_views
from .users import seed_users, undo_users
from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        undo_projects()
        undo_favorites()
        undo_comments()
        undo_instructions()
        undo_supplies()
        undo_views()
        undo_users()
    # Before seeding, truncate all tables prefixed with schema name
        # db.session.execute(f"TRUNCATE table {SCHEMA}.project RESTART IDENTITY CASCADE;")
        # db.session.execute(f"TRUNCATE table {SCHEMA}.favorites RESTART IDENTITY CASCADE;")
        # db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
        # db.session.execute(f"TRUNCATE table {SCHEMA}.instructions RESTART IDENTITY CASCADE;")
        # db.session.execute(f"TRUNCATE table {SCHEMA}.supplies RESTART IDENTITY CASCADE;")
        # db.session.execute(f"TRUNCATE table {SCHEMA}.views RESTART IDENTITY CASCADE;")
        # db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
        # Add other undo functions here
        # Add a truncate command here for every table that will be seeded.
        # db.session.commit()
        
    # Add other seed functions here
    seed_users()
    seed_views()
    seed_supplies()
    seed_instructions()
    seed_comments()
    seed_favorites()
    seed_project()



# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    # Add other undo functions here
    undo_projects()
    undo_instructions()
    undo_supplies()
    undo_comments()
    undo_views()
    undo_favorites()
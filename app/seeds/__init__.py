from flask.cli import AppGroup
from app.seeds.favorite import seed_favorites, undo_favorites
from app.seeds.instruction_seeder import seed_instructions, undo_instructions
from app.seeds.supply_seeder import seed_supplies, undo_supplies
from app.seeds.comment_seeder import seed_comments, undo_comments

from app.seeds.projects_seeder import seed_project, undo_project
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
    # Before seeding, truncate all tables prefixed with schema name
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
        # Add a truncate command here for every table that will be seeded.
        db.session.commit()
    seed_users()
    seed_users()
    # Add other seed functions here
    seed_project()
    seed_instructions()
    seed_supplies()
    seed_comments()
    seed_views()
    seed_favorites()



# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    # Add other undo functions here
    undo_project()
    undo_instructions()
    undo_supplies()
    undo_comments()
    undo_views()
    undo_favorites()
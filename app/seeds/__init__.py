from flask.cli import AppGroup
from app.seeds.instruction_seeds import instruction_seed, undo_instructions

from app.seeds.projects import seed_project, undo_project_seeders
from .users import seed_users, undo_users

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    # Add other seed functions here
    seed_project()
    instruction_seed()



# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    # Add other undo functions here
    undo_project_seeders()
    undo_instructions()
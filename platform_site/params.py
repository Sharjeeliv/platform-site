import os

DB_NAME = "database.db"
PARAMS = {
    'SECRET_KEY': os.environ['PL_SECRET_KEY'],
    'DB_URI': f'sqlite:///{DB_NAME}',
    'TOKEN': os.environ['PL_TOKEN']
}
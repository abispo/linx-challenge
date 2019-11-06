import databases
import orm
import sqlalchemy

from decouple import config

TESTING = config('LINX_CHALLENGE_TESTING', cast=bool)

if TESTING:
    database = databases.Database('sqlite:///test.db', force_rollback=True)
else:
    database = databases.Database(config('DATABASE_URL'))

metadata = sqlalchemy.MetaData()

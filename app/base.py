import databases
import orm
import sqlalchemy

from decouple import config

database = databases.Database(config('DATABASE_URL'))
metadata = sqlalchemy.MetaData()

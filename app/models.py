import orm

from app.base import database, metadata


class APIResponse(orm.Model):
    __tablename__ = 'tb_api_response'
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    timestamp_start = orm.Float(allow_null=False, precision=5)
    timestamp_end = orm.Float(allow_null=False, precision=5)
    ip_address = orm.String(max_length=100, allow_null=False)
    api_response = orm.JSON(allow_null=False)
    city = orm.String(max_length=100, allow_null=False)

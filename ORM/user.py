from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class User(Model):
    __table_name__ = "users"
    id = columns.Integer(primary_key=True)
    name = columns.Text()
    age = columns.Integer()
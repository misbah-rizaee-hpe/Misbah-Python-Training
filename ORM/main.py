from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from user import User
from utils import new_user

# Connect to the Cassandra cluster
connection.setup(['127.0.0.1'], "cqlengine", protocol_version=3)

# Sync the User model with the database
sync_table(User)

# Create a user
user = new_user(user_id=1, name='Alice', age=25)

# Query the user table
users = User.objects.all()
print([user for user in users])
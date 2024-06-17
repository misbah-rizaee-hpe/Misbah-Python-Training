import csv
from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('cqlengine')  # Connect to your keyspace

# CSV file path
csv_file = 'Files/import_data.csv'

# Open the CSV file for reading
with open(csv_file, 'r', newline='') as f:
    reader = csv.reader(f)
    
    # Skip header row
    next(reader)  # Skip the header row if it exists
    
    # Iterate over rows in the CSV file
    for row in reader:
        user_id = int(row[0])   # Assuming id is the first column and an integer
        name = row[1]           # Assuming name is the second column
        age = int(row[2])       # Assuming age is the third column and an integer
        
        # Insert row into Cassandra table
        query = "INSERT INTO users (id, name, age) VALUES (%s, %s, %s)"
        session.execute(query, (user_id, name, age))

print(f"Data imported from {csv_file} into Cassandra")
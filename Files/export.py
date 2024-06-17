import csv
from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('cqlengine')  # Connect to your keyspace

# Query data from Cassandra
query = "SELECT * FROM users;"
rows = session.execute(query)

# Define CSV file path
csv_file = 'Files/exported_data.csv'

# Using csv.writer to write data to CSV file
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    
    # Write header row (optional)
    writer.writerow(['id', 'name', 'age'])  # Adjust column names as per your table schema
    
    # Write data rows
    for row in rows:
        writer.writerow([row.id, row.name, row.age])  # Adjust fields as per your table columns

print(f"Data exported to {csv_file}")

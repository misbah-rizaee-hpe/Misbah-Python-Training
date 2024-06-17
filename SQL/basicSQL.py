import sqlite3

# Connect to the database
conn = sqlite3.connect('SQL/example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert a row
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
conn.commit()

# Query the table
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Close the connection
conn.close()
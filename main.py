# Script to create a sample sqlite3 database with a set of randomly generated users. Showcases the use of basic SQL for creating and extracting data.

import sqlite3
import random

# Function to generate a random name
def generate_random_name():
    first_names = ['Yuki', 'Hiroshi', 'Sakura', 'Naoko', 'Kenji', 'Ayumi', 'Takeshi', 'Yui', 'Daiki', 'Riko']
    last_names = ['Sato', 'Suzuki', 'Takahashi', 'Tanaka', 'Watanabe', 'Ito', 'Nakamura', 'Kobayashi', 'Yamamoto', 'Kato']
    
    return random.choice(first_names) + " " + random.choice(last_names)

# Connect to the database (or create one if it doesn't exist)
connection = sqlite3.connect('test_database.db')

# Create a cursor object
cursor = connection.cursor()

# Delete the table if it exists
cursor.execute("DROP TABLE IF EXISTS users")

# Create a table
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    );"""
)

# Insert a large set of random data
for _ in range(100):  # Insert 100 random users
    name = generate_random_name()
    age = random.randint(15, 65)
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

# Commit (save) changes
connection.commit()

# Retrieve data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Display retrieved data
print("\nRandomly generated users:\n")
for row in rows:
    print(row)
print()

# Close the connection
connection.close()

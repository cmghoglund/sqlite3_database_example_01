# Script to create a sample sqlite3 database with a set of randomly generated users. Showcases the use of basic SQL for creating and extracting data.

import sqlite3
import random

# Function to generate a random name
def generate_random_name():
    first_names = ['Yuki', 'Hiroshi', 'Sakura', 'Naoko', 'Kenji', 'Ayumi', 'Takeshi', 'Yui', 'Daiki', 'Riko']
    last_names = ['Sato', 'Suzuki', 'Takahashi', 'Tanaka', 'Watanabe', 'Ito', 'Nakamura', 'Kobayashi', 'Yamamoto', 'Kato']
    return random.choice(first_names) + " " + random.choice(last_names)

# Function to generate a random email
def generate_random_email(name):
    domains = ['example.co.jp', 'mail.jp', 'webmail.jp']
    return name.lower().replace(' ', '.') + '@' + random.choice(domains)

# Function to generate a random city
def generate_random_city():
    cities = ['Tokyo', 'Osaka', 'Nagoya', 'Sapporo', 'Fukuoka', 'Kobe', 'Yokohama', 'Kyoto', 'Hiroshima', 'Sendai']
    return random.choice(cities)

# Connect to the database (or create one if it doesn't exist)
connection = sqlite3.connect('test_database.db')

# Create a cursor object
cursor = connection.cursor()

# Delete the table if it exists
cursor.execute("DROP TABLE IF EXISTS users;")

# Create a table
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        email TEXT,
        city TEXT,
        is_employee BOOLEAN
        );"""
)

# Generate data for several thousand users
user_data = []

for _ in range(5000):  # Insert 5000 random users
    name = generate_random_name()
    age = random.randint(15, 65)
    email = generate_random_email(name)
    city = generate_random_city()
    is_employee = random.choice([True, False])

    user_data.append((name, age, email, city, is_employee))

# Insert data in a single batch using the executemany() method
cursor.executemany("""
    INSERT INTO users (name, age, email, city, is_employee)
    VALUES (?, ?, ?, ?, ?);""", user_data
)

# Commit (save) changes
connection.commit()

# Retrieve data
cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()

# Display retrieved data
print("\nRandomly generated users:\n")
for row in rows:
    print(row)
print()

# Close the connection
connection.close()

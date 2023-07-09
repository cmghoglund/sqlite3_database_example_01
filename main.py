# Script to create a sample sqlite3 database with a set of randomly generated users. Showcases the use of basic SQL for creating and extracting data.

import sqlite3
import random

def generate_random_name():
    first_names = ['Yuki', 'Hiroshi', 'Sakura', 'Naoko', 'Kenji', 'Ayumi', 'Takeshi', 'Yui', 'Daiki', 'Riko']
    last_names = ['Sato', 'Suzuki', 'Takahashi', 'Tanaka', 'Watanabe', 'Ito', 'Nakamura', 'Kobayashi', 'Yamamoto', 'Kato']
    return random.choice(first_names) + " " + random.choice(last_names)

def generate_random_email(name):
    domains = ['example.co.jp', 'mail.jp', 'webmail.jp']
    return name.lower().replace(' ', '.') + '@' + random.choice(domains)

def generate_random_city():
    cities = ['Tokyo', 'Osaka', 'Nagoya', 'Sapporo', 'Fukuoka', 'Kobe', 'Yokohama', 'Kyoto', 'Hiroshima', 'Sendai']
    return random.choice(cities)

def create_table(cursor):
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

def insert_random_users(cursor, num_users):
    user_data = []

    for _ in range(num_users):
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

def main():
    # Connect to the database (or create one if it doesn't exist)
    connection = sqlite3.connect('test_database.db')
    # Create a cursor object
    cursor = connection.cursor()

    create_table(cursor)

    # Start a transaction (wrapping the inserts within a transaction reduces the time it takes to write to the database)
    connection.execute("BEGIN TRANSACTION")

    # Insert 5000 random users
    insert_random_users(cursor, 5000)

    # Commit the transaction
    connection.commit()

    # Retrieve and display the first 10 rows
    cursor.execute("SELECT * FROM users LIMIT 10;")
    rows = cursor.fetchall()

    print("\nFirst 10 rows:\n")
    for row in rows:
        print(row)
    print()

    """
    Execute a more complex SQL query to do the following:
    - display the names and emails of users who are employees, aged between 25 and 30, and are living in either Tokyo or Osaka
    - order the results by city in ascending order and then by age in descending order
    """ 
    cursor.execute("""
        SELECT name, email
        FROM users
        WHERE is_employee = 1
            AND age BETWEEN 25 AND 30
            AND city IN ('Tokyo', 'Osaka')
        ORDER BY city ASC, age DESC
    """)

    # Fetch the results
    results = cursor.fetchall()

    # Display the results
    print("Names and emails of employees aged between 25 and 30, living in Tokyo or Osaka:\n")
    for row in results:
        print(row)
    print()

    # Close the connection
    connection.close()

if __name__ == "__main__":
    main()

# Script to create a sample sqlite3 database with a set of randomly generated users. Showcases the use of basic SQL for creating and extracting data.

import sqlite3
import random
import datetime

def generate_random_name():
    first_names = ['Yuki', 'Hiroshi', 'Sakura', 'Naoko', 'Kenji', 'Ayumi', 'Takeshi', 'Yui', 'Daiki', 'Riko']
    last_names = ['Sato', 'Suzuki', 'Takahashi', 'Tanaka', 'Watanabe', 'Ito', 'Nakamura', 'Kobayashi', 'Yamamoto', 'Kato']
    return random.choice(first_names) + " " + random.choice(last_names)

def generate_random_age():
    return random.randint(15, 65)

def generate_random_email(name):
    domains = ['example.co.jp', 'mail.jp', 'webmail.jp']
    return name.lower().replace(' ', '.') + '@' + random.choice(domains)

def generate_random_city():
    cities = ['Tokyo', 'Osaka', 'Nagoya', 'Sapporo', 'Fukuoka', 'Kobe', 'Yokohama', 'Kyoto', 'Hiroshima', 'Sendai']
    return random.choice(cities)

def generate_random_employee_status():
    return random.choice([True, False])

# Helper function to generate 4-digit sections for random phone numbers
def generate_random_four_digits():
    return ''.join(str(random.randint(0, 9)) for _ in range(4))

def generate_random_phone_number():
    return f"080-{generate_random_four_digits()}-{generate_random_four_digits()}"  # Japanese phone number format (assumes only mobile phone numbers, all starting with 080)

def generate_random_join_date():
    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date.today()
    time_between_dates = end_date - start_date
    random_number_of_days = random.randrange(time_between_dates.days)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")

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
            is_employee BOOLEAN,
            phone_number TEXT,
            join_date TEXT
            );
    """)

def insert_random_users(cursor, num_users):
    user_data = []

    for _ in range(num_users):
        name = generate_random_name()
        age = generate_random_age()
        email = generate_random_email(name)
        city = generate_random_city()
        is_employee = generate_random_employee_status()
        phone_number = generate_random_phone_number()
        join_date = generate_random_join_date()

        user_data.append((name, age, email, city, is_employee, phone_number, join_date))

    # Insert data in a single batch using the executemany() method
    cursor.executemany("""
        INSERT INTO users (name, age, email, city, is_employee, phone_number, join_date)
        VALUES (?, ?, ?, ?, ?, ?, ?);
    """, user_data)

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

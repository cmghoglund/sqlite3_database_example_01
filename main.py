# Script to create a sample sqlite3 database with a set of randomly generated users. Showcases the use of basic SQL for creating and extracting data.

import sqlite3
import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_random_gender():
    return random.choice(['Male', 'Female'])

def generate_random_name(gender):
    # 50 Japanese male first names
    male_first_names = [
        'Hiroshi', 'Kenji', 'Takeshi', 'Daiki', 'Yusuke', 'Yudai', 'Shota', 'Ryota', 'Kazuki', 'Kenta', 
        'Yoshiro', 'Nobu', 'Issei', 'Kosuke', 'Yuji', 'Kohei', 'Toshi', 'Sora', 'Haruki', 'Makoto', 
        'Ryosuke', 'Takuya', 'Shinji', 'Riku', 'Masato', 'Junichi', 'Satoshi', 'Daisuke', 'Hideo', 'Ryoma', 
        'Yuya', 'Tomohiro', 'Naoki', 'Manabu', 'Hidetoshi', 'Tetsuya', 'Masahiro', 'Noriyuki', 'Tatsuya', 'Toru', 
        'Shinobu', 'Yutaka', 'Keiichi', 'Hiroaki', 'Fumio', 'Ryoichi', 'Tadashi', 'Minoru', 'Akio', 'Yasushi'
    ]

    # 50 Japanese female first names
    female_first_names = [
        'Yuki', 'Sakura', 'Naoko', 'Ayumi', 'Yui', 'Riko', 'Mai', 'Akiko', 'Haruka', 'Aiko', 
        'Rina', 'Miho', 'Kana', 'Eri', 'Sayaka', 'Yuka', 'Misaki', 'Keiko', 'Manami', 'Saki', 
        'Tomomi', 'Maki', 'Natsuki', 'Yoshiko', 'Asuka', 'Risa', 'Mami', 'Hitomi', 'Kaori', 'Yuriko', 
        'Emi', 'Chie', 'Nanami', 'Noriko', 'Rei', 'Sachiko', 'Ayano', 'Megumi', 'Yoko', 'Kumiko', 
        'Miki', 'Aya', 'Mari', 'Nozomi', 'Shizuka', 'Airi', 'Yumi', 'Hikari', 'Kazumi', 'Mariko'
    ]

    # 50 Japanese last names
    last_names = [
        'Sato', 'Suzuki', 'Takahashi', 'Tanaka', 'Watanabe', 'Ito', 'Nakamura', 'Kobayashi', 'Yamamoto', 'Kato', 
        'Yoshida', 'Yamada', 'Sasaki', 'Yamaguchi', 'Saito', 'Matsumoto', 'Inoue', 'Kimura', 'Hayashi', 'Shimizu', 
        'Yamazaki', 'Mori', 'Abe', 'Ikeda', 'Hashimoto', 'Ishikawa', 'Yamashita', 'Ogawa', 'Ishii', 'Hasegawa', 
        'Maeda', 'Fujita', 'Okada', 'Goto', 'Kondo', 'Ishida', 'Ueda', 'Miyazaki', 'Endo', 'Fujii', 
        'Matsuda', 'Asano', 'Noguchi', 'Murakami', 'Ono', 'Takeuchi', 'Miyamoto', 'Fukuda', 'Uchida', 'Sakai'
    ]

    if gender == 'Male':
        return random.choice(male_first_names) + " " + random.choice(last_names)
    else:
        return random.choice(female_first_names) + " " + random.choice(last_names)

def generate_random_age():
    return random.randint(15, 65)

def generate_random_email(name):
    # 50 fictional Japanese domain names
    domains = [
        'example.co.jp', 'mail.jp', 'webmail.jp', 'tokyotech.jp', 'sushilove.jp', 
        'mangamania.jp', 'animerama.jp', 'nihongolearn.jp', 'japanesecrafts.jp', 'bentoexpress.jp', 
        'kimonokawaii.jp', 'techkyoto.jp', 'jpopwave.jp', 'nihongobridge.jp', 'japanesesnacks.jp', 
        'origamiart.jp', 'samuraicode.jp', 'nihongotalk.jp', 'greenteashop.jp', 'tunaclub.jp', 
        'animegarden.jp', 'ninjalifestyle.jp', 'otakulife.jp', 'ramenking.jp', 'bonsaiworld.jp', 
        'japanesetech.jp', 'gameninja.jp', 'mochimagic.jp', 'toriirestaurant.jp', 'kabukiview.jp', 
        'cherryblossom.jp', 'tanukitown.jp', 'kaijufun.jp', 'virtualtokyo.jp', 'totoroshop.jp', 
        'matchamania.jp', 'sakesommelier.jp', 'shibainu.jp', 'otakufan.jp', 'yakisoba.jp', 
        'ikebanadreams.jp', 'haikulove.jp', 'robotmuseum.jp', 'karaokeparty.jp', 'yokaiyarn.jp', 
        'onsenspa.jp', 'fujisanart.jp', 'sumoworld.jp', 'sushimaster.jp', 'haikuhaven.jp'
    ]

    return name.lower().replace(' ', '.') + '@' + random.choice(domains)

def generate_random_city():
    # 50 Japanese city names
    cities = [
        'Tokyo', 'Osaka', 'Nagoya', 'Sapporo', 'Fukuoka', 'Kobe', 'Yokohama', 'Kyoto', 'Hiroshima', 'Sendai', 
        'Naha', 'Kawasaki', 'Sakai', 'Kumamoto', 'Okayama', 'Hamamatsu', 'Hachioji', 'Niigata', 'Fukushima', 'Kanazawa', 
        'Nagasaki', 'Miyazaki', 'Matsuyama', 'Shizuoka', 'Akita', 'Chiba', 'Toyama', 'Nara', 'Yokosuka', 'Maebashi', 
        'Mito', 'Utsunomiya', 'Oita', 'Kitakyushu', 'Takamatsu', 'Kochi', 'Tottori', 'Matsue', 'Kagoshima', 'Asahikawa', 
        'Yamagata', 'Toyohashi', 'Kurashiki', 'Yamaguchi', 'Iwaki', 'Koriyama', 'Wakayama', 'Sasebo', 'Hakodate', 'Takasaki'
    ]

    return random.choice(cities)

def generate_random_employee_status():
    return random.choice([True, False])

# Helper function to generate 4-digit sections for random phone numbers
def generate_random_four_digits():
    return ''.join(str(random.randint(0, 9)) for _ in range(4))

def generate_random_phone_number():
    # Japanese phone number format (assumes only mobile phone numbers, all starting with 080)
    return f"080-{generate_random_four_digits()}-{generate_random_four_digits()}"

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
    # TODO Arrange table fields in more logical order
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
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
        gender = generate_random_gender()
        name = generate_random_name(gender)
        age = generate_random_age()
        email = generate_random_email(name)
        city = generate_random_city()
        is_employee = generate_random_employee_status()
        phone_number = generate_random_phone_number()
        join_date = generate_random_join_date()

        user_data.append((name, age, gender, email, city, is_employee, phone_number, join_date))

    # Insert data in a single batch using the executemany() method
    cursor.executemany("""
        INSERT INTO users (name, age, gender, email, city, is_employee, phone_number, join_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
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

    # Query to get the number of users in each city
    query = """
    SELECT city, COUNT(*) as num_users
    FROM users
    GROUP BY city
    ORDER BY num_users DESC
    LIMIT 5;
    """

    # Read the data into a pandas DataFrame
    data = pd.read_sql_query(query, connection)

    # Plot the data using Matplotlib
    data.plot(kind='bar', x='city', y='num_users', legend=None)
    plt.xlabel('City')
    plt.ylabel('Number of Users')
    plt.title('Top 5 Cities by Number of Users')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot
    plt.show()

    # Plot the data using Seaborn
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(x='city', y='num_users', data=data)
    ax.set(xlabel='City', ylabel='Number of Users', title='Top 5 Cities by Number of Users')
    sns.despine()

    # Show the plot
    plt.show()

    # Close the connection
    connection.close()

if __name__ == "__main__":
    main()

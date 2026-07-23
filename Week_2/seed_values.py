from database import setup_database

def seed_value():
    conn= setup_database()
    cursor=conn.cursor()

    books=[
        ("Obstacle is the way", 1),
        ("Ego is the enemy", 0),
        ("Tuesday with morrie", 0),
        ("Atomic Habits", 1),
        ("Metamorphosis", 1),
        ("Yogi", 0)
    ]

    cursor.executemany(
        """
        INSERT INTO books
        (title, availability)
        VALUES (?, ?)
        ON CONFLICT(title) DO NOTHING
        """, books
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    seed_value()
    print("Books inserted successfully.")
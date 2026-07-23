import sqlite3

DATABASE_NAME="tasks.db"

#@ setting up databases:
def setup_database():
    conn=sqlite3.connect(DATABASE_NAME)
    conn.row_factory= sqlite3.Row
    return conn

#@ creating a table:
def create_table():
    conn=setup_database()
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE NOT NULL,
            availability BOOLEAN NOT NULL)"""
    )
    conn.commit()
    conn.close()

if __name__=="__main__":
    create_table()
    print("Successfully created db and tables")
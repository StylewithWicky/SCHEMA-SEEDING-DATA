import sqlite3

conn=sqlite3 .connect('book.db')
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Author(
               id INTERGER PRIMARY KEY,name TEXT,birth_year INTERGER
               )

            ''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS Genre(
               id INTERGER PRIMARY KEY,
               name TEXT UNIQUE NOT NULL

               )
            ''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books(
               id INTEGER PRIMARY KEY,
               title TEXT NOT NULL,
               FOREIGN KEY(author_id) REFERENCE Author(id),
               FOREIGN KEY(genre_id) REFERENCE Genre(id),
               year_published INTERGER
               )          

                ''')
conn.commit()
conn.close()
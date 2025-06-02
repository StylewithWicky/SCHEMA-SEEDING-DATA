import sqlite3

conn=sqlite3 .connect('book.db')
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Author(
               id INTEGER PRIMARY KEY,name TEXT,birth_year INTERGER
               )

            ''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS Genre(
               id INTEGER PRIMARY KEY,
               name TEXT UNIQUE NOT NULL

               )
            ''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS Publisher(
              id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               author_id INTEGER NOT NULL,
               genre_id INTEGER NOT NULL,
               year_published INTEGER NOT NULL,
               FOREIGN KEY (author_id) REFERENCE Author(id),
               FOREIGN KEY (genre_id) REFERENCE Genre(id)

               )
                
            ''')
conn.commit()
conn.close()
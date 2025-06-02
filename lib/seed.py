import sqlite3

conn=sqlite3 .connect('book.db')
cursor=conn.cursor()

#seeding into Author
cursor.execute("INSERT INTO Author (id,name,birth_year) VALUES (?,?,?)",(1,'J.K. Rowling',1965))
cursor.execute("INSERT INTO Author (id,name,birth_year) VALUES (?,?,?)",(2,'George Orwell',1903))
cursor.execute("INSERT INTO Author (id,name,birth_year) VALUES (?,?,?)",(3,'Jane Austen',1775))

#Seeding into Genre
cursor.execute("INSERT INTO Genre (id,name) VALUES (?,?)",(1,'Fantasy'))
cursor.execute("INSERT INTO Genre (id,name) VALUES (?,?)",(2,'Dystopian'))
cursor.execute("INSERT INTO Genre (id,name) VALUES (?,?)",(3,'Romance'))

#Seeding into Publisher
cursor.execute("INSERT INTO Publisher (id,name,author_id,genre_id,year_published) VALUES(?,?,?,?,?)", (1,'Peter Parker',1, 1, 1778))
cursor.execute("INSERT INTO Publisher (id,name,author_id,genre_id,year_published) VALUES(?,?,?,?,?)", (2,'Barry Allen',2, 2, 1978))
cursor.execute("INSERT INTO Publisher (id,name,author_id,genre_id,year_published) VALUES(?,?,?,?,?)", (3,'Louise Lane',3, 3, 1788))
conn.commit()
conn.close()
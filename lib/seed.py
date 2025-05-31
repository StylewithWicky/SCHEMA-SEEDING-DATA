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

#Seeding into Books
cursor.execute('INSERT INTO BOOKS (id,title,author_id,genre_id,year_published) VALUE (?,?,?,?,?)',(1,'Harry Potter and the Sorcerer’s Stone',1,1,1990))
cursor.execute('INSERT INTO BOOKS (id,title,author_id,genre_id,year_published) VALUE (?,?,?,?,?)',(1,'Harry Potter and the Sorcerer’s Stone',1,1,1980))
cursor.execute('INSERT INTO BOOKS (id,title,author_id,genre_id,year_published) VALUE (?,?,?,?,?)',(1,'Harry Potter and the Sorcerer’s Stone',1,1,1950))
conn.commit()
import sqlite3

# Connect to the seeded database
conn = sqlite3.connect('book.db')
cursor = conn.cursor()

# Test 1: Check tables exist
tables = ['Author', 'Genre', 'Books']
for table in tables:
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
    result = cursor.fetchone()
    assert result is not None, f"❌ Table {table} does NOT exist!"
    print(f"✅ Table {table} exists.")

# Test 2: Check if 3 authors were inserted
cursor.execute("SELECT COUNT(*) FROM Author")
author_count = cursor.fetchone()[0]
assert author_count == 3, f"❌ Expected 3 authors, found {author_count}"
print("✅ 3 authors found.")

# Test 3: Check if 3 genres were inserted
cursor.execute("SELECT COUNT(*) FROM Genre")
genre_count = cursor.fetchone()[0]
assert genre_count == 3, f"❌ Expected 3 genres, found {genre_count}"
print("✅ 3 genres found.")

# Test 4: Check if 3 books were inserted
cursor.execute("SELECT COUNT(*) FROM Books")
book_count = cursor.fetchone()[0]
assert book_count == 3, f"❌ Expected 3 books, found {book_count}"
print("✅ 3 books found.")

# Test 5: Check if foreign key values are valid
cursor.execute('''
    SELECT Books.title, Author.name, Genre.name
    FROM Books
    JOIN Author ON Books.author_id = Author.id
    JOIN Genre ON Books.genre_id = Genre.id
''')
books = cursor.fetchall()
assert len(books) == 3, f"❌ Book relations are broken."
print("✅ All books are linked to valid authors and genres.")

conn.close()

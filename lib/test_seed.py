import sqlite3

DB_PATH = 'book.db'


#this is to test if there is author table
def test_author_table():
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    tables=['Author']
    for table in tables:
        cursor.execute(f"SELECT name  FROM sqlite_master WHERE type='table' AND name=? ", (table,))
        result=cursor.fetchone()
        assert result is not None, f"Table {table} does not exist!"
    conn.close()
def test_genre_table():
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    tables=['Genre']
    for table in tables:
        cursor.execute(f"SELECT name  FROM sqlite_master WHERE type='table' AND name=? ", (table,))
        result=cursor.fetchone()
        assert result is not None, f"Table {table} does not exist!"
    conn.close()
def test_publisher_table():
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    tables=['Publisher']
    for table in tables:
        cursor.execute(f"SELECT name  FROM sqlite_master WHERE type='table' AND name=? ", (table,))
        result=cursor.fetchone()
        assert result is not None, f"Table {table} does not exist!"
    conn.close()

# I Want to check the number of authors
def test_author_count():
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM Author")
    author_count=cursor.fetchone()[0]
    assert author_count <= 3, f"Expected 3 authors, found {author_count}"
    conn.close()

def test_genres_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Genre")
    genre_count = cursor.fetchone()[0]
    assert genre_count <= 3, f"❌ Expected 3 genres, found {genre_count}"
    conn.close()

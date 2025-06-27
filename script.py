import sqlite3

connection = sqlite3.connect('book_db.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
books(book_id INTEGER PRIMARY KEY, title TEXT, 
      authorFName TEXT, authorLName TEXT, publicationDate INTEGER, pages INTEGER)"""

cursor.execute(command1)

command2 = """CREATE TABLE IF NOT EXISTS
userBookList(userID INTEGER PRIMARY KEY, book_id INTEGER, FOREIGN KEY(book_id) REFERENCES books(book_id))"""

cursor.execute(command2)


command3 = """CREATE TABLE IF NOT EXISTS
userAccountInfo(userID INTEGER PRIMARY KEY, userFName TEXT, userLName TEXT, userPWord TEXT)"""

cursor.execute(command3)

cursor.execute("INSERT INTO books VALUES (1232, 'Between Two Fires', 'Gabe', 'Gabriel', 1999, 784)")

cursor.execute("SELECT * FROM books")

results = cursor.fetchall()

print(results)
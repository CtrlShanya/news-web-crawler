##### Database and table creation and testing code #####
import sqlite3

connection = sqlite3.connect("News.db")
cursor = connection.cursor()

# to make a new table:
# this table already exists, so the execution of the command is commented out

# cursor.execute("CREATE TABLE test1 (subtitle TEXT NOT NULL PRIMARY KEY, title TEXT, abstract TEXT, download_time TIMESTAMP, update_time TIMESTAMP);")

# to check all the tables currently existing in the News.db:
tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("Tables: ", tables)

# printing all rows from 'test1' table:
rows = cursor.execute("SELECT * FROM test1;").fetchall()
print("Rows: ")
for row in rows:
	print(row, "\n")
	
connection.close()



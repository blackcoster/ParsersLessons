import sqlite3

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()
cursorObj.execute('SELECT * FROM workers')
rows = cursorObj.fetchall()
for row in rows:
    print(row)

import sqlite3

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()
cursorObj.execute('SELECT id,name FROM workers WHERE salary > 0.0')
rows = cursorObj.fetchall()
print(len(rows))
for row in rows:
    print(row)
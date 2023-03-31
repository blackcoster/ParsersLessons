import sqlite3

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()
cursorObj.execute('SELECT name FROM sqlite_master where type="table"')
print(cursorObj.fetchall())

# выводит название таблиц в базе данных

import sqlite3

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()
cursorObj.execute('UPDATE workers SET salary = 1200 WHERE id = 2')
con.commit()
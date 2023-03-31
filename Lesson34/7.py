import sqlite3
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()

cursorObj.execute('CREATE TABLE IF NOT EXISTS projects (id integer, name text)')
con.commit()

# cursorObj.execute('DROP TABLE IF EXISTS projects')
# con.commit()

# cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "workers" ')
# print(cursorObj.fetchall())

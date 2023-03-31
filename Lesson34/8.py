import sqlite3
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()

cursorObj.execute('DROP TABLE IF EXISTS workers')
con.commit()

cursorObj = con.cursor()
cursorObj.execute('DROP TABLE IF EXISTS projects')
con.commit()
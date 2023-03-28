import os
import sqlite3
db_filename = 'todo.db'
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)
if db_is_new:
    print('создана новая база')
else:
    print('уже существует')

conn.close()
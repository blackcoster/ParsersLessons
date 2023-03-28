import os
import sqlite3
db_filename = 'todo.db'
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)

# cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS users (
#         passport INT PRIMARY KEY,
#         name TEXT,
#         gender TEXT);
# """)
# conn.commit()

# cur = conn.cursor()
# cur.execute("""insert into users (passport, name, gender)
#        values ('123', 'polina','woman');
# """)
# conn.commit()

cur = conn.cursor()
cur.execute("""SELECT * FROM users;
""")
conn.commit()
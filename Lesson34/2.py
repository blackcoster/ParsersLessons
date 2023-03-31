import sqlite3

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()
cursorObj.execute(
                  "INSERT INTO workers(id, name, salary, department, position, hireDate) VALUES (1, 'John',700,'HR','Manager','2017-01-04')")
con.commit()
stroka = (2, 'Polina',100500,'Tech','Programmer','2019-07-04')
cursorObj.execute(
                  "INSERT INTO workers(id, name, salary, department, position, hireDate) VALUES (?,?,?,?,?,?)",stroka)
con.commit()
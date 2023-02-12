#ignore this for now, it is just a reference 
import sqlite3

connection = sqlite3.connect("data.db")

crsr = connection.cursor()
 
# print statement will execute if there
# are no errors
print("Connected to the database")
 
sql_command = """CREATE TABLE `article` (
  `Title` VARCHAR(100) NOT NULL,
  `Summary` VARCHAR(1000) NOT NULL,
  `Topic` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`Title`))"""

sql_command2 = '''INSERT INTO article VALUES(?, ?, ?)'''
values = 'OWKR', 'testing', 'tester'
crsr.execute(sql_command)
crsr.execute(sql_command2, values)
#print(crsr.fetchall())
#print(sqlite3.version)
#print(sqlite3.sqlite_version)
# close the connection
connection.commit()

connection.close()

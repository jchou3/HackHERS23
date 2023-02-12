import sqlite3

connection = sqlite3.connect("articles.db")

crsr = connection.cursor()
 
# print statement will execute if there
# are no errors
print("Connected to the database")
 
sql_command = """CREATE TABLE `article` (
  `articleID` INT NOT NULL,
  `title` VARCHAR(100) NOT NULL,
  `summary` VARCHAR(1000) NOT NULL,
  `topic` VARCHAR(50) NOT NULL,
  `type` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`articleID`))"""

sql_command2 = """CREATE TABLE `full_text` (
  `articleID` INT NOT NULL,
  `text` TEXT(2000) NOT NULL,
  PRIMARY KEY (`articleID`))"""
  
crsr.execute(sql_command)
crsr.execute(sql_command2)
#print(crsr.fetchall())
#print(sqlite3.version)
#print(sqlite3.sqlite_version)
# close the connection
connection.commit()

connection.close()

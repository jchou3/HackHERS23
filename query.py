import sqlite3

connection = sqlite3.connect("data.db")

crsr = connection.cursor()

#test = ['onehg', 'twohh', 'threesss']

def addArticle(array):
    sql_command2 = '''INSERT INTO article VALUES(?, ?, ?)'''
    values = array[0], array[1], array[2]
    crsr.execute(sql_command2, values)

#addArticle(test)

comm = '''SELECT * FROM article'''
crsr.execute(comm)
print(crsr.fetchall())
connection.commit()
connection.close()

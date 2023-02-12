import sqlite3
connection = sqlite3.connect("databases/data.db")
crsr = connection.cursor()
query = """SELECT * FROM News WHERE Topic = ?"""
result = crsr.execute(query, 'Politics')
res = crsr.fetchall()
for i in res:
    print(i[2])
connection.commit()
connection.close()
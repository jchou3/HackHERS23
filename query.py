import sqlite3

connection = sqlite3.connect("databases/data.db")

crsr = connection.cursor()

res = crsr.execute("""SELECT *  
                FROM News
                """)

for i in res: 
    print(crsr.fetchone())
    connection.commit()
    connection.close()
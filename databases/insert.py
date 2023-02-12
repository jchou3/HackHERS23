import sqlite3
import pandas as pd

connection = sqlite3.connect("data.db")

data = pd.read_csv("databases/News.csv")

# sql_command = """CREATE TABLE `News` (
#   `index` INT NOT NULL,
#   `Title` VARCHAR(100) NOT NULL,
#   `Summary` VARCHAR(1000) NOT NULL,
#   `Topic` VARCHAR(50) NOT NULL,
#   PRIMARY KEY (`index`))"""

crsr = connection.cursor()

#crsr.execute(sql_command)

data.to_sql(
    'News',
    connection,
    if_exists="replace"
)

#print(data.iloc[0:4,0])

# for i in range(len(data)):
#     query = "INSET INTO News VALUES(?, ?, ?)"
#     values = i
#     row = data.iloc[i]
#     print()
    #crsr.execute(

# crsr.execute('''SELECT * FROM News
#                 ''')

# print(crsr.fetchone())

connection.commit()

connection.close()

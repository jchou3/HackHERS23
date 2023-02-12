import sqlite3
import pandas as pd

connection = sqlite3.connect("data.db")

data = pd.read_csv("databases/News.csv")
#print(data.columns)
data.to_sql(
    'News',
    connection,
    if_exists='replace'
)

crsr = connection.cursor()

crsr.execute('''SELECT (index) FROM article
                ''')

print(crsr.fetchone())

connection.commit()

connection.close()

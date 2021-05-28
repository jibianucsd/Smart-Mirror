import mysql.connector as mysql

import os
from dotenv import load_dotenv
load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

try:
  cursor.execute("""
    CREATE TABLE List (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      todo        TEXT DEFAULT NULL,
      created_at  TIMESTAMP
    );
  """)
except:
  print("List table already exists. Not recreating it.")

query = "insert into List (todo, created_at) values (%s, %s)"
values = [
  ('ECE140B Project', '2021-05-16 12:00:00')
]
cursor.executemany(query, values)
db.commit()

cursor.execute("select * from List;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]
db.close()
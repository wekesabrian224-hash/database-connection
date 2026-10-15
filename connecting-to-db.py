import sqlite3
import pandas as pd
import sqlite3 
conn = sqlite3.connect('data.sqlite')

cur = conn.cursor()

 Execute the query

# (This is a special query for finding the table names. You don't need to memorize it.)

# SQLite databases all have a sqlite_master table that stores the schema information

cur.execute("""SELECT name FROM sqlite_master WHERE type = 'table';""")

# Fetch the result and store it in table_names

#table_names = cur.fetchall()

#table_names

[('orderdetails',),
 ('payments',),
 ('offices',),
 ('customers',),
 ('orders',),
 ('productlines',),
 ('products',),
 ('employees',)]
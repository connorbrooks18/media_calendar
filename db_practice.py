import sqlite3 as sql

conn = sql.connect("media.db")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
            name1 TEXT, 
            name2 TEXT, 
            email TEXT NOT NULL UNIQUE, 
            e_pass TEXT NOT NULL
            )""")

print(cur.execute("SELECT * FROM users").fetchall())


cur.close()
conn.close()

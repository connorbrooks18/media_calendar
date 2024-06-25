import sqlite3 as sql

conn = sql.connect("media.db")

cur = conn.cursor()

cur.execute("CREATE TABLE media (name TEXT)")
cur.execute("CREATE TABLE users (email TEXT, e_pass TEXT)")

rows = cur.execute("SELECT rowid, name FROM media").fetchall()
print(rows)


cur.close()
conn.close()
import sqlite3 as sql

conn = sql.connect("media.db")

cur = conn.cursor()

# cur.execute("CREATE TABLE media (name TEXT)")
 
cur.execute("INSERT INTO media VALUES ('JJK')")
cur.execute("INSERT INTO media VALUES ('ONE PIECE')")

rows = cur.execute ("SELECT rowid, name FROM media").fetchall()
print(rows)
cur.close()
conn.close()
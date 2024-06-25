# import sqlite3 as sql

# conn = sql.connect("media.db")

# cur = conn.cursor()

# cur.execute("CREATE TABLE users (email TEXT, e_pass TEXT)")

# rows = cur.execute("SELECT rowid, name FROM media").fetchall()
# print(rows)


# cur.close()
# conn.close()

from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("key", "w") as f:
    f.write(str(key))
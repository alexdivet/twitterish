import sqlite3

conn = sqlite3.connect('twitterish.db')

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS twitterish (name, datetime, tweet)")

c.execute("INSERT INTO twitterish VALUES ('Marty McFly', '100', 'First tweet!')")

c.execute("SELECT * FROM twitterish")
print(c.fetchall())

conn.commit()

conn.close()

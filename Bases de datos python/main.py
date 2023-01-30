import sqlite3 as db
conn = db.connect("miaplicacion.db");
cursor = conn.cursor();
rows = cursor.execute("SELECT * FROM users");
for row in rows:
    print(row)
cursor.close();
conn.close();
import sqlite3 as db
conn = db.connect("database.db", isolation_level=None);
cursor = conn.cursor();
nombre = "sopi"
query = f"SELECT * FROM Alumnos WHERE nombre = '{nombre.title()}'"
ress = cursor.execute(query)
for i in ress:
    print(i)
cursor.close();
conn.close();
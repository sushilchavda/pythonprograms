import sqlite3

conn = sqlite3.connect("student.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER, name TEXT, marks INTEGER)")
cur.execute("DELETE FROM student")

cur.execute("INSERT INTO student VALUES (1, 'Amit', 78)")
cur.execute("INSERT INTO student VALUES (2, 'Riya', 85)")
cur.execute("INSERT INTO student VALUES (3, 'Neha', 92)")
conn.commit()
print("Records inserted")

cur.execute("UPDATE student SET marks = 80 WHERE id = 1")
conn.commit()
print("Record updated")

cur.execute("DELETE FROM student WHERE id = 3")
conn.commit()
print("Record deleted")

cur.execute("SELECT * FROM student")
for row in cur.fetchall():
    print(row)

conn.close()

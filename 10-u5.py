import sqlite3

conn = sqlite3.connect("student.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER, name TEXT, marks INTEGER)")
cur.execute("DELETE FROM student")
students = [(1, "Amit", 78), (2, "Riya", 85), (3, "Neha", 92),
            (4, "Raj", 67), (5, "Kiran", 88)]
cur.executemany("INSERT INTO student VALUES (?, ?, ?)", students)
conn.commit()

cur.execute("SELECT * FROM student")
print("fetchone():")
print(cur.fetchone())

cur.execute("SELECT * FROM student")
print("\nfetchmany(2):")
for row in cur.fetchmany(2):
    print(row)

cur.execute("SELECT * FROM student")
print("\nfetchall():")
for row in cur.fetchall():
    print(row)

conn.close()

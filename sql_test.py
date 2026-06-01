import sqlite3

# Connect to Database
conn = sqlite3.connect("database/students.db")

# Create Cursor
cursor = conn.cursor()

print("\n===== TOTAL STUDENTS =====")

cursor.execute("""
SELECT COUNT(*)
FROM students
""")

total_students = cursor.fetchone()[0]

print("Total Students:", total_students)

# --------------------------------------------------

print("\n===== AVERAGE CGPA =====")

cursor.execute("""
SELECT AVG(CGPA)
FROM students
""")

avg_cgpa = cursor.fetchone()[0]

print("Average CGPA:", round(avg_cgpa, 2))

# --------------------------------------------------

print("\n===== PLACED STUDENTS =====")

cursor.execute("""
SELECT *
FROM students
WHERE Placed='Yes'
""")

placed_students = cursor.fetchall()

for student in placed_students:
    print(student)

# --------------------------------------------------

print("\n===== NOT PLACED STUDENTS =====")

cursor.execute("""
SELECT *
FROM students
WHERE Placed='No'
""")

not_placed = cursor.fetchall()

for student in not_placed:
    print(student)

# --------------------------------------------------

print("\n===== TOP PERFORMER =====")

cursor.execute("""
SELECT *
FROM students
ORDER BY CGPA DESC
LIMIT 1
""")

top_student = cursor.fetchone()

print(top_student)

# --------------------------------------------------

print("\n===== PLACEMENT SUMMARY =====")

cursor.execute("""
SELECT Placed,
       COUNT(*)
FROM students
GROUP BY Placed
""")

summary = cursor.fetchall()

for row in summary:
    print(row)

# --------------------------------------------------

print("\n===== STUDENTS WITH CGPA > 8 =====")

cursor.execute("""
SELECT Name, CGPA
FROM students
WHERE CGPA > 8
""")

high_cgpa_students = cursor.fetchall()

for student in high_cgpa_students:
    print(student)

# --------------------------------------------------

print("\n===== STUDENTS SORTED BY CGPA =====")

cursor.execute("""
SELECT Name, CGPA
FROM students
ORDER BY CGPA DESC
""")

sorted_students = cursor.fetchall()

for student in sorted_students:
    print(student)

# --------------------------------------------------

# Close Connection
conn.close()

print("\nDatabase Connection Closed")
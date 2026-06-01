from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():

    conn = sqlite3.connect("database/students.db")
    cursor = conn.cursor()

    # Total Students
    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )
    total_students = cursor.fetchone()[0]


    cursor.execute(
        "SELECT AVG(CGPA) FROM students"
    )
    avg_cgpa = round(cursor.fetchone()[0], 2)


    cursor.execute(
        """
        SELECT COUNT(*)
        FROM students
        WHERE Placed='Yes'
        """
    )

    placed_students = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        total_students=total_students,
        avg_cgpa=avg_cgpa,
        placed_students=placed_students
    )

if __name__ == "__main__":
    app.run(debug=True)
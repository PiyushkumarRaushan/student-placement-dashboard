import sqlite3
import pandas as pd

df = pd.read_csv("students.csv")

conn = sqlite3.connect("database/students.db")

df.to_sql(
    "students",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database Created Successfully!")
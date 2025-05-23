import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="airflow_user",
    password="Helee279",
    database="airflow_db"
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES;")
for table in cursor:
    print(table)

conn.close()

import psycopg2
from config import config

confs = config()
conn = psycopg2.connect(**confs)
try:
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        print(f"Server version: {cur.fetchone()}")

    with conn.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE phonebook(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            phone_number VARCHAR(25) NOT NULL)"""
        )
        print("Table created succesfully")

except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if conn:
        conn.close()
        print("PostgreSQL connection close")
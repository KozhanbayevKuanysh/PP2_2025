import psycopg2
from config import config

try:
    confs = config()
    connection = psycopg2.connect(**confs)
    
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE NOT NULL)"""
        )
        cursor.execute(
        """CREATE TABLE user_scores (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        level INTEGER NOT NULL,
        score INTEGER NOT NULL);"""
        )
        print("Table created successfully")  


except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if connection:
        connection.close()
        print("PostgreSQL connection closed")
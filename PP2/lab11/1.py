import psycopg2
from config import config

conf = config()
connection = psycopg2.connect(**conf)

def execute_query(query):
    try:
        with connection.cursor() as cur:
            cur.execute(query)
            connection.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

create_func_search = f"""CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
    RETURNS TABLE(id INT, first_name VARCHAR(255), phone_number VARCHAR(25))
    AS $$
    BEGIN
        RETURN QUERY
        SELECT * FROM phonebook 
        WHERE phonebook.first_name ILIKE '%' || pattern || '%' 
            OR phonebook.phone_number ILIKE '%' || pattern || '%';
    END;
    $$ LANGUAGE plpgsql;"""

# execute_query(create_func_search)

create_proc_insert = f"""CREATE OR REPLACE PROCEDURE insert_or_update(user_name TEXT, user_phone TEXT)
    AS $$
    BEGIN
        UPDATE phonebook
        SET phone_number = user_phone
        WHERE first_name = user_name;

        IF NOT FOUND THEN
            INSERT INTO phonebook(first_name, phone_number)
            VALUES (user_name, user_phone);
        END IF;
    END;
    $$ LANGUAGE plpgsql;"""

# execute_query(create_proc_insert)

create_proc_delete = f"""CREATE OR REPLACE PROCEDURE delete_user(input TEXT)
    AS $$
    BEGIN
        DELETE FROM phonebook
        WHERE first_name = input OR phone_number = input;
    END;
    $$ LANGUAGE plpgsql;"""

# execute_query(create_proc_delete)
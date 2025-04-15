import psycopg2
import os
import csv
from config import config

conf = config()
connection = psycopg2.connect(**conf)

cursor = connection.cursor()

mode = int(input("Select mode:\n1-add data from consol\n2-add data from csv file\n3-update data\n4-query data\n5-delete data\nEnter: "))

if mode == 1:
    data = []
    name = input("Enter name: ")
    number = input("Enter number: ")
    data.append([name ,number])
    for dat in data:
        cursor.execute(f"INSERT INTO phonebook (first_name, phone_number) VALUES ('{dat[0]}', {dat[1]})")
    
    connection.commit()
    print("Done")

elif mode == 2:
    path = input("Enter the csv file path: ")
    data = []
    if not os.path.exists(path):
        print("Error: Path does not exists")
    
    with open(path) as file:
        row = csv.reader(file)
        next(row)

        for dat in row:
            data.append(dat)

    for row in data:
        cursor.execute(f"INSERT INTO phonebook (first_name, phone_number) VALUES ('{row[0]}', {row[1]})")

    connection.commit()
    print("Done")

elif mode == 3:
    pname = input("Enter name of contact: ")
    pnumber = input("Enter number of contact: ")

    cursor.execute(f"SELECT * FROM phonebook WHERE first_name = '{pname}' AND phone_number = '{pnumber}'")
    if cursor.rowcount == 0:
        print("Contact does not exist")

    else:
        what = input("name - to update name\nnum - to update number\nEnter: ")
        if what not in ['num', 'name']:
            print("ERROR")

        else:
            if what == 'name':
                newcontact = str(input(f"Enter new name: "))
                cursor.execute(f"UPDATE phonebook SET first_name = '{newcontact}' WHERE phone_number = '{pnumber}'")

            elif what == 'num':
                newcontact = input("Enter new number: ")
                cursor.execute(f"UPDATE phonebook SET phone_number = {newcontact} WHERE first_name = '{pname}'")

            else: print("ERROR")

            connection.commit()
            print("Done")

elif mode == 4:
    how = int(input(
    "Choose query mode:\n1 - search by first_name\n2 - search by phone_number\n3 - query all rows\nEnter: "
    ))

    if how not in [1, 2, 3]:
        print("ERROR")

    value = input("Enter query: ")
    query_dict = {
        1 : f"WHERE first_name = '{value}'",
        2 : f"WHERE phone_number = {value}",
        3 : f""
    }

    cursor.execute(f"SELECT * FROM phonebook {query_dict[how]}")

    result = cursor.fetchall()
    if len(result) == 0:
        print("No result")
    else:
        print("Results: ")
    
    for row in result:
        print(row)

elif mode == 5:
    how = input("Select mode:\nname - delete by name\nnum - delete by number\nEnter: ")

    if how == 'name':
        name5 = str(input("Enter name: "))
        cursor.execute(f"DELETE FROM phonebook WHERE first_name = '{name5}'")

    elif how == 'num':
        phone = input(f"Enter number: ")
        cursor.execute(f"DELETE FROM phonebook WHERE phone_number = {phone}")
    
    else: print("ERROR")

    connection.commit()
    print("Done")

else: print("ERROR")

connection.close()
cursor.close()
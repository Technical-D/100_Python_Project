# User Management System
import psycopg2
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()

def db_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="users",
            user=os.getenv("user"),
            password=os.getenv("password"),
            port=5432
        )
        cursor = connection.cursor()
        return connection, cursor
    except Exception as e:
        print(f"An error occured: {e}")
    
    return None, None

def add_user():
    connection, cursor = db_connection()
    if connection and cursor:
        print("Add user:")
        while True:
            username = input("Username: ")
            query = f"select user_id from users where username=%s;"
            cursor.execute(query,(username,))
            result = cursor.fetchall()
            if result:
                print("Username is taken! Try another username.")
                continue
            break

        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        
        while True:
            age = input("Age: ")
            try:
                age = int(age)
                break
            except ValueError:
                print("Please enter a valid age!")
        
        while True:
            gender = input("Gender(M/F): ").lower()
            if gender in ['male','m']:
                gender = "Male"
            elif gender in ['female', 'f']:
                gender = "Female"
            else:
                print("Please enter a valid gender!")
                continue
            break

        query = f"insert into users(username, first_name, last_name, age, gender) values(%s, %s, %s, %s, %s);"
        cursor.execute(query, (username, first_name, last_name, age, gender))
        if cursor.rowcount > 0:
            print("User added to system sucessfully!")

        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Sorry for inconvenience!")
        print("Our database is not working currently. Try again after sometime.")

def retrieve_user_info():
    connection, cursor = db_connection()
    if connection and cursor:
        print("Fetch user information:")
        while True:
            username = input("Please enter the username: ")
            query = f"select * from users where username='{username}';"
            cursor.execute(query)
            user_info = cursor.fetchall()
            if user_info:
                print("\nUser's Information:-")
                print(f"Username: {user_info[0][1]}\nFirst Name: {user_info[0][2]}\nLast Name: {user_info[0][3]}\nAge: {user_info[0][4]}\nGender: {user_info[0][5]}")
                sleep(2)
            else:
                print("User info not found! Check your username.")
                continue
            break

        cursor.close()
        connection.close()
    else:
        print("Sorry for inconvenience!")
        print("Our database is not working currently. Try again after sometime.")

def main():
    print("-" * 40)
    print("Welcome to User Management System!")
    print("-" * 40)
    while True:
        menu = """
Please choose an option:
1. Add a new user to the system
2. Fetch User Details
3. Exit
        """
        print(menu)
        choice = int(input("Enter your choice(1-3): "))
        if choice == 1:
            add_user()
        elif choice == 2:
            retrieve_user_info()
        else:
            print("Sayonara!")
            break

if __name__ == "__main__":
    main()
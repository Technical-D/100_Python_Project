# User Management System
import psycopg2

def db_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="users",
            user="postgres",
            password="dheeraj1902",
            port=5432
        )
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        print(f"An error occured: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()

def add_user():
    cusrsor = db_connection()
    print("Add user:")
    while True:
        username = input("Username: ")
        query = "select user_id from users where username='{username}';"
        cusrsor.execute(query)
        result = cusrsor.fetchall()
        if not result:
            print("Username is taken! Try again.")
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

    query = f"insert into users(username, first_name, last_name, age, gender) values('{username}', '{first_name}', '{last_name}', {age}, '{gender}');"
    cusrsor.execute(query)
    if cusrsor.rowcount > 0:
        print("User added to system sucessfully!")

def main():
    print("-" * 20)
    print("Welcome to User Management System!")
    print("-" * 20)
    while True:
        menu = """
        Please choose an option:
        1. Add a new user to the system
        2. Search for a user
        3. Exit
        """
        print(menu)
        choice = int(input("Enter your choice(1-3): "))
        if choice == 1:
            add_user()
        elif choice == 2:
            pass
        else:
            print("Sayonara!")
            break

main()
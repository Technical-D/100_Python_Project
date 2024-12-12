# Conatct Management System
import json 

def add_person():
    name = input("Name: ")
    while True:
        try:
            age = int(input("Age: "))
            break
        except:
            print("Invalid age!")

    email = input("Email: ")
    person = {"name":name, "age":age, "email":email}

    return person

def display_people(people):
    print("Sr", "->", " Name ", "|"," Age ","|", " Email ")
    for i, person in enumerate(people):
        print(i+1, " ->", person["name"], "|",person["age"],"|", person["email"])

def delete_contact(people):
    display_people(people)

    while True:
        number = input("Enter the number of conatct you want to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number. Out of range!")
            else:
                break
        except:
            print("Invalid Number!")
    
    people.pop(number - 1)
    print("Person deleted!") 

def search(people):
    results = []
    while True:
        search_by = input("Search by name or email: ").lower()
        if search_by == "name":
            search_name = input('Search for a name: ').lower()
            for person in people:
                name = person["name"]
                if search_name in name.lower():
                    results.append(person)
            break
        elif search_by == "email":
            search_email = input('Search for a email: ').lower()
            for person in people:
                email = person["email"]
                if search_email in email.lower():
                    results.append(person)
            break
        else:
            print("Invalid search category.")
            continue
    display_people(results)

print("Hi, welcome to the Contact Management System.")

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print()
    print("Contact list siz: ", len(people))
    command = input("You can 'Add', 'Delete' or 'Search' and 'q' for quit: ").lower()

    if command == 'add':
        person = add_person()
        people.append(person)
        print("Person Added!")
    elif command == 'delete':
        delete_contact(people)
    elif command == 'search':
        search(people)
    elif command == 'q':
        break
    else:
        print("Inavlid Command!")

display_people(people)

with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)
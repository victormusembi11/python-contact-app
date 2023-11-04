"""Main file for the application."""
from app.view import create_contact, delete_contact, view_contacts

while True:
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        view_contacts()
    elif choice == "2":
        create_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        break
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")

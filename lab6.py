#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 09:16:20 2023

@author: mshk
"""


contact_list = [
    {"name": "Ali", "number": "001"},
    {"name": "Joe", "number": "002"},
]


def view_contacts(contact_list):
    print("....View Contacts.....")
    for index, contact in enumerate(contact_list):
        print(f"{index + 1} {contact['name']} {contact['number']}")


def add_contacts():
    global contact_list
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contact_info = {"name": name, "number": number}
    contact_list.append(contact_info)
    print(f"{name} - {number} has been added to the contact list")


def delete_contact():
    global contact_list  # Access the global contact_list

    contact_id = int(input("Enter the ID of the contact to delete: "))

    for index, contact in enumerate(contact_list):
        try:
            print(
                f"Contact id {contact_id} {contact_list[contact_id - 1]['name']} {contact_list[contact_id - 1]['number']} has been deleted"
            )
            contact_list.pop(contact_id - 1)
            break
        except IndexError:
            print(f"Invalid Id! No contact with ID {contact_id} found")


def main():
    while True:
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Select an option (1/2/3/4): ")

        if choice == "1":
            view_contacts(contact_list)
        elif choice == "2":
            add_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

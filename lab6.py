#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 09:16:20 2023

@author: mshk
"""

# if __name__ = '__main__':
#     main()
    
    
contact_list = ["Ahmed", "001", "Ali", "002", "John", "003"]

def view_contacts():
    view_list = []
    for i in range(0, len(view_list), 2):
        name = view_list[i]
        number = view_list[i + 1]
        contact_id = i // 2 + 1
        contact_info = f"{contact_id} {name} {number}"
        view_list.append(contact_info)
    return view_list

def add_contacts():
    add_list = contact_list
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contact_info = [name, number]
    add_list.append(contact_info)
    print(f"{name} - {number} has been added to the contact list")

def delete_contact():
    global contact_list  # Access the global contact_list

    contact_id = input("Enter the ID of the contact to delete: ")

    contact_found = False

    for i in range(0, len(contact_list), 3):
        name = contact_list[i]
        number = contact_list[i + 1]
        current_id = contact_list[i + 2]

        if current_id == contact_id:
            contact_found = True
            contact_list.pop(i)      
            contact_list.pop(i)      
            contact_list.pop(i)      
            print(f"Contact with ID {contact_id} - {name} - {number} has been deleted")
            break

    if not contact_found:
        print(f"No contact found with ID {contact_id}")

# Main program
while True:
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Select an option (1/2/3/4): ")

    if choice == "1":
        contacts = view_contacts()
        for contact in contacts:
            print(contact)
    elif choice == "2":
        add_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        break
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")




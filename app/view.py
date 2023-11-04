"""All the functions that are used to interact with the user are defined here."""
from app.models import Contact
from config.db_conn import cnx


def create_contact() -> None:
    """Create a contact."""
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contact = Contact(cnx)
    contact.add_contact(name, number)


def view_contacts() -> None:
    """View all contacts.""" ""
    contact = Contact(cnx)
    result = contact.get_contacts()
    for contact in result:
        print(f"{contact[0]} {contact[1]} {contact[2]}")


def delete_contact() -> None:
    """Delete a contact."""
    contact_id = int(input("Enter the ID of the contact to delete: "))
    contact = Contact(cnx)
    contact.delete_contact(contact_id)

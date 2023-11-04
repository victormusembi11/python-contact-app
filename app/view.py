from config.db_conn import cnx
from app.models import Contact


def create_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contact = Contact(cnx)
    contact.add_contact(name, number)

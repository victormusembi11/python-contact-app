"""All the database models are defined here."""


class Contact:
    """Contact model."""

    def __init__(self, cnx: object) -> object:
        """Initialize the Contact model."""
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def add_contact(self, name: str, phone: str):
        """Add a contact to the database."""
        query = "INSERT INTO Contacts (name, phone) VALUES (%s, %s)"
        values = (name, phone)
        self.cursor.execute(query, values)
        self.cnx.commit()
        print(f"{name} - {phone} has been added to the contact list")

    def get_contacts(self):
        """Get all contacts from the database."""
        query = "SELECT * FROM Contacts"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def delete_contact(self, contact_id: int):
        """Delete a contact from the database."""
        query = "DELETE FROM Contacts WHERE id = %s"
        values = (contact_id,)
        self.cursor.execute(query, values)
        self.cnx.commit()
        print(f"Contact id {contact_id} has been deleted")

class Contact:
    def __init__(self, cnx: object) -> object:
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def add_contact(self, name: str, phone: str):
        query = "INSERT INTO Contacts (name, phone) VALUES (%s, %s)"
        values = (name, phone)
        self.cursor.execute(query, values)
        self.cnx.commit()
        print(f"{name} - {phone} has been added to the contact list")

    def get_contacts(self):
        query = "SELECT * FROM Contacts"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

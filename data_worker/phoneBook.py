from .contact import Contact

class Book:

    def __init__(self, name: str = "Contacts book", contact_list: list = None):
        if contact_list is None:
            contact_list = []
        self.name = name
        self.contact_list = contact_list

    def add_contact(self, contact: Contact):
        self.contact_list.append(contact)

    def remove_contact(self, contact: Contact):
        self.contact_list.remove(contact)

    def get_contacts(self, path):
        with open(path, 'r', encoding = 'utf8') as contact_data:
            for contact in contact_data:
                contact = contact.strip().split(',')
                self.add_contact(Contact(*contact))

    def __str__(self):
        result_str = f"\nContact book: "
        for i, contact in enumerate(self.contact_list):
            result_str += f"\n{i + 1}: \nName: {contact.name}\n" \
                          f"Family name: {contact.fam_name}\n" \
                          f"Phone: {contact.phone}"
        return result_str

    def update_book(self, update_list, path):
        with open(path, 'a+', encoding='utf8') as contact_data:
            contact_data.write(update_list)

import tkinter as tk
import os

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        os.system('cls')
        print("Contact added successfully.")
        print("Added Contact Details:")
        print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def view_contacts(self):
        if len(self.contacts) == 0:
            os.system('cls')
            print("No contacts found.")
        else:
            os.system('cls')
            for contact in self.contacts:
               
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        if len(found_contacts) == 0:
            os.system('cls')
            print("No matching contacts found.")
        else:
            for contact in found_contacts:
                os.system('cls')
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def update_contact(self, contact, new_name, new_phone_number, new_email, new_address):
        old_name = input("Enter the name of the contact you want to update: ")
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_name
                contact.phone_number = new_phone_number
                contact.email = new_email
                contact.address = new_address
                os.system('cls')
                print("Contact updated successfully.")
                return
        os.system('cls')
        print("Contact not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                return f"Contact {name} deleted successfully."
        return "Contact not found."

    def show_gui(self):
        root = tk.Tk()
        root.title("Contact Book")

        # Create labels and entry fields for contact details
        name_label = tk.Label(root, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(root)
        name_entry.pack()

        phone_label = tk.Label(root, text="Phone Number:")
        phone_label.pack()
        phone_entry = tk.Entry(root)
        phone_entry.pack()

        email_label = tk.Label(root, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(root)
        email_entry.pack()

        address_label = tk.Label(root, text="Address:")
        address_label.pack()
        address_entry = tk.Entry(root)
        address_entry.pack()

        # Create buttons for adding, viewing, searching, updating, and deleting contacts
        add_button = tk.Button(root, text="Add Contact", command=lambda: self.add_contact(Contact(name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get())))
        add_button.pack()

        view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        view_button.pack()

        search_button = tk.Button(root, text="Search Contact", command=lambda: self.search_contact(name_entry.get()))
        search_button.pack()

        update_button = tk.Button(root, text="Update Contact", command=lambda: self.update_contact(Contact(name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get()), name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get()))
        update_button.pack()

        delete_button = tk.Button(root, text="Delete Contact", command=lambda: self.delete_contact(name_entry.get()))
        delete_button.pack()

        

        root.mainloop()



# Create an instance of ContactManager
contact_manager = ContactManager()

# Show the GUI
contact_manager.show_gui()

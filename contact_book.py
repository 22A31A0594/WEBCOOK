import json

contact = {}

def display_contact():
    print("Contact Book:")
    print("----------------")
    print("Name\t\tContact Number\t\tEmail\t\tAddress")
    for key, value in contact.items():
        print(f"{key}\t\t{value['phone']}\t\t{value['email']}\t\t{value['address']}")

def add_contact():
    name = input("Enter the contact name: ")
    phone = input("Enter the mobile number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    contact[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact {name} added successfully!")

def search_contact():
    search_name = input("Enter the contact name: ")
    if search_name in contact:
        print(f"{search_name}'s contact details:")
        print(f"Phone: {contact[search_name]['phone']}")
        print(f"Email: {contact[search_name]['email']}")
        print(f"Address: {contact[search_name]['address']}")
    else:
        print("Name is not found in contact book")

def edit_contact():
    edit_contact = input("Enter the contact to be edited: ")
    if edit_contact in contact:
        phone = input("Enter new mobile number (press Enter to skip): ")
        email = input("Enter new email (press Enter to skip): ")
        address = input("Enter new address (press Enter to skip): ")
        if phone:
            contact[edit_contact]['phone'] = phone
        if email:
            contact[edit_contact]['email'] = email
        if address:
            contact[edit_contact]['address'] = address
        print(f"Contact {edit_contact} updated successfully!")
        display_contact()
    else:
        print("Name is not found in contact book")

def delete_contact():
    del_contact = input("Enter the contact to be deleted: ")
    if del_contact in contact:
        confirm = input("Do you want to delete this contact? (y/n): ")
        if confirm.lower() == 'y':
            contact.pop(del_contact)
            print(f"Contact {del_contact} deleted successfully!")
            display_contact()
        else:
            print("Deletion cancelled")
    else:
        print("Name is not found in contact book")

def export_contacts():
    with open('contacts.json', 'w') as f:
        json.dump(contact, f)
    print("Contacts exported to contacts.json successfully!")

def import_contacts():
    try:
        with open('contacts.json', 'r') as f:
            imported_contacts = json.load(f)
            global contact
            contact = imported_contacts
            print("Contacts imported from contacts.json successfully!")
    except FileNotFoundError:
        print("The file contacts.json does not exist.")
    except json.JSONDecodeError:
        print("Error decoding JSON from file contacts.json.")

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add new contact")
    print("2. Search contact")
    print("3. Display contacts")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Export contacts")
    print("7. Import contacts")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact()
    elif choice == 4:
        edit_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        export_contacts()
    elif choice == 7:
        import_contacts()
    elif choice == 8:
        break
    else:
        print("Invalid choice. Please try again.")

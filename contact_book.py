contacts = {}

while True:
    print("\n----- CONTACT BOOK -----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            for name, details in contacts.items():
                print("\nName:", name)
                print("Phone:", details["Phone"])
                print("Email:", details["Email"])
                print("Address:", details["Address"])

    elif choice == "3":
        name = input("Enter name to search: ")

        if name in contacts:
            print("\nName:", name)
            print("Phone:", contacts[name]["Phone"])
            print("Email:", contacts[name]["Email"])
            print("Address:", contacts[name]["Address"])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to update: ")

        if name in contacts:
            contacts[name]["Phone"] = input("Enter new phone number: ")
            contacts[name]["Email"] = input("Enter new email: ")
            contacts[name]["Address"] = input("Enter new address: ")
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice.")
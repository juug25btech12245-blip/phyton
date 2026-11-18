contacts = []  # list of dictionaries

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")

def search_contact():
    key = input("Enter name to search: ").strip().lower()
    found = [c for c in contacts if key in c["name"].lower()]
    if found:
        for c in found:
            print(c)
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ").strip().lower()
    for c in contacts:
        if c["name"].lower() == name:
            c["phone"] = input("New phone: ").strip()
            c["email"] = input("New email: ").strip()
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip().lower()
    for c in contacts:
        if c["name"].lower() == name:
            contacts.remove(c)
            print("Contact deleted.")
            return
    print("Contact not found.")

while True:
    print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
    ch = input("Choice: ")
    if ch == "1": add_contact()
    elif ch == "2": view_contacts()
    elif ch == "3": search_contact()
    elif ch == "4": update_contact()
    elif ch == "5": delete_contact()
    elif ch == "6": break
    else: print("Invalid choice.")

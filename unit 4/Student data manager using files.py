FILE = "students.txt"

def add_student():
    roll = input("Roll no: ")
    name = input("Name: ")
    marks = input("Marks: ")
    with open(FILE, "a") as f:
        f.write(f"{roll},{name},{marks}\n")
    print("Student saved.")

def view_students():
    try:
        with open(FILE, "r") as f:
            print(f"{'Roll':<8}{'Name':<15}{'Marks'}")
            for line in f:
                roll, name, marks = line.strip().split(",")
                print(f"{roll:<8}{name:<15}{marks}")
    except FileNotFoundError:
        print("No data file yet.")

def search_student():
    key = input("Enter roll no: ")
    try:
        with open(FILE) as f:
            for line in f:
                if line.split(",")[0] == key:
                    print("Found:", line.strip())
                    return
        print("Not found.")
    except FileNotFoundError:
        print("No data file yet.")

def delete_student():
    key = input("Enter roll no to delete: ")
    try:
        with open(FILE) as f:
            lines = f.readlines()
        with open(FILE, "w") as f:
            deleted = False
            for line in lines:
                if line.split(",")[0] == key:
                    deleted = True
                else:
                    f.write(line)
        print("Deleted." if deleted else "Not found.")
    except FileNotFoundError:
        print("No data file yet.")

while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
    ch = input("Choice: ")
    if ch == "1": add_student()
    elif ch == "2": view_students()
    elif ch == "3": search_student()
    elif ch == "4": delete_student()
    elif ch == "5": break
    else: print("Invalid choice.")

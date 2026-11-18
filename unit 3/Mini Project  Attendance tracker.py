from datetime import datetime

attendance = {}  # {date: {student: "P"/"A"}}
students = ["Asha", "Ravi", "Meena", "John"]

def mark_attendance():
    date = datetime.now().strftime("%d-%m-%Y")
    attendance[date] = {}
    for s in students:
        status = input(f"{s} (P/A): ").strip().upper()
        while status not in ("P", "A"):
            status = input("Enter P or A: ").strip().upper()
        attendance[date][s] = status
    print("Attendance saved for", date)

def view_attendance():
    if not attendance:
        print("No records.")
        return
    for date, rec in attendance.items():
        print("\nDate:", date)
        for s, st in rec.items():
            print(f"  {s}: {st}")

def percentage():
    total_days = len(attendance)
    if total_days == 0:
        print("No records.")
        return
    for s in students:
        present = sum(1 for rec in attendance.values() if rec.get(s) == "P")
        pct = present / total_days * 100
        flag = "" if pct >= 75 else "  <- Shortage"
        print(f"{s}: {present}/{total_days} = {pct:.1f}%{flag}")

while True:
    print("\n1.Mark 2.View 3.Percentage 4.Exit")
    ch = input("Choice: ")
    if ch == "1": mark_attendance()
    elif ch == "2": view_attendance()
    elif ch == "3": percentage()
    elif ch == "4": break
    else: print("Invalid choice.")

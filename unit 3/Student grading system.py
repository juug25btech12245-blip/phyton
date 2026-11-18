def get_grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    elif avg >= 50: return "D"
    else: return "F"

students = {}  # name -> list of marks

n = int(input("Number of students: "))
for _ in range(n):
    name = input("Student name: ")
    marks = list(map(int, input("Enter marks of 3 subjects (space separated): ").split()))
    students[name] = marks

print(f"\n{'Name':<15}{'Total':<8}{'Average':<10}{'Grade'}")
for name, marks in students.items():
    total = sum(marks)
    avg = total / len(marks)
    print(f"{name:<15}{total:<8}{avg:<10.2f}{get_grade(avg)}")

topper = max(students, key=lambda s: sum(students[s]))
print("\nTopper:", topper, "with total", sum(students[topper]))

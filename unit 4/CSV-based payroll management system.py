import csv

employees = [
    ["emp_id", "name", "basic"],
    [101, "Asha", 40000],
    [102, "Ravi", 55000],
    [103, "Meena", 30000],
]
with open("employees.csv", "w", newline="") as f:
    csv.writer(f).writerows(employees)

def calculate(basic):
    hra = 0.20 * basic
    da = 0.10 * basic
    pf = 0.12 * basic
    tax = 0.10 * basic if basic > 50000 else 0
    gross = basic + hra + da
    net = gross - pf - tax
    return hra, da, pf, tax, gross, net

try:
    with open("employees.csv", newline="") as fin, \
         open("payroll.csv", "w", newline="") as fout:
        reader = csv.DictReader(fin)
        writer = csv.writer(fout)
        writer.writerow(["emp_id", "name", "basic", "hra", "da", "pf", "tax", "gross", "net"])
        for row in reader:
            basic = float(row["basic"])
            hra, da, pf, tax, gross, net = calculate(basic)
            writer.writerow([row["emp_id"], row["name"], basic, hra, da, pf, tax, gross, net])
            print(f"{row['name']:<8} Gross: {gross:>10.2f}   Net: {net:>10.2f}")
    print("\nPayroll saved to payroll.csv")
except FileNotFoundError:
    print("Employee file missing.")
except ValueError:
    print("Invalid salary value in file.")

print("UNIT CONVERTER")

print("1. Kilometer to Meter")
print("2. Meter to Kilometer")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

if choice == 1:
    km = float(input("Enter kilometers: "))
    meter = km * 1000
    print("Meters =", meter)

elif choice == 2:
    meter = float(input("Enter meters: "))
    km = meter / 1000
    print("Kilometers =", km)

elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print("Fahrenheit =", f)

elif choice == 4:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Celsius =", c)

else:
    print("Invalid choice")

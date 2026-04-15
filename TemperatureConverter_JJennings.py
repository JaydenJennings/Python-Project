print("Temperature converter")
print("Units C = Celsius, F = Fahrenheit, K = Kelvin")


# function to convert TO celsius
def to_celsius(temp, from_unit):
    if from_unit == "C":
        return temp
    elif from_unit == "F":
        return (temp - 32) * 5/9
    elif from_unit == "K":
        return temp - 273.15


# function to convert FROM celsius
def from_celsius(celsius, to_unit):
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return (celsius * 9/5) + 32
    elif to_unit == "K":
        return celsius + 273.15



running = True

while running:

    try:
        temp = float(input("Enter temperature value: "))
    except ValueError:
        print("Invalid number.")
        continue

    from_unit = input("Enter input unit (C/F/K): ").upper()
    to_unit = input("Enter output unit (C/F/K): ").upper()

    if from_unit not in ["C", "F", "K"] or to_unit not in ["C", "F", "K"]:
        print("Invalid unit.")
        continue

    if from_unit == "K" and temp < 0:
        print("Kelvin cannot be negative.")
        continue

    celsius = to_celsius(temp, from_unit)

    result = from_celsius(celsius, to_unit)

    print(f"Result: {result:.2f} {to_unit}")

    choice = input("Convert again? (yes/no): ").lower()

    if choice == "no":
        running = False



weight = float(input("Enter your weight"))
unit = input("Kilograms or pounds? (K or L)")

if unit == "K":
    weight = weight * 2.205
elif unit == "Lbs":
    weight = weight / 2.05
    unit = "Kgs."
else:
    print(f"{unit} was not valid")

print(f"your weight is: {round(weight, 1)} {unit}")

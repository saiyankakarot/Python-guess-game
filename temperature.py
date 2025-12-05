unit = input("Is this remperature in Celsius or Fahrenheit(c/f): ")
temp = float(input("Enter the temperature: "))

if unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}F")
elif unit == "f":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}C")
else:
    print(f"{unit} is an invalid unit of measurement")

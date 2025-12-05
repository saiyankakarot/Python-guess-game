principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
if principal <= 0:
    print("Principal can't be less than or equal to zero")

    while rate <= 0:
     rate = float(input("Enter the Intrest rate: "))
if rate <= 0:
    print("Intrest  rate can't be less than or equal to zero")

    while time <= 0:
        time = int(input("Enter the time in year: "))
if time <= 0:
    print("Time can't be less than or equal to zero")

    print(principal)
    print(rate)
    print(time)
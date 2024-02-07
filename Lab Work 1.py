"""
    Program Purpose: To ask user to input data and calculate the surface area base on the given formula
    and types of shapes (cubes, sphere & cylinder).
    Programmer: Muhamad Azfar Bin Mohamad Fauzi
    Date: 7 February 2024
"""

# Prompt the user to choose the types of exchange rates
print("Currency Conversion Program")
print("Exchange rates:")
print("USD - US Dollar: 0.25")
print("EUR - Euro: 0.21")
print("GBP - British Pound: 0.18")
print("---------------------------")
print("Choose the taret currency:")
print("1. USD - US Dollar")
print("2. EUR - Euro")
print("3. GBP - British Pound")
print("---------------------------")

usd = 0.25
eur = 0.21
gbp = 0.18

#Input from the user will be assigned to the variable named choice
choice = int(input("Enter your choice (1 - 3): "))

if choice == 1:  # To calculate usd malaysia ringgit
    amnt = float(input("Enter the amount in Malaysia Ringgit (MYR): "))
    total = amnt * usd
    print("Equivalent amount in US Dollar (USD): RM", total)

elif choice == 2:  # To calculate euro to myr
    amnt = float(input("Enter the amount in Malaysia Ringgit (MYR): "))
    total = amnt * eur
    print("Equivalent amount in US Euro (EUR): RM", total)

elif choice == 3:  # To calculate gbp to myr
    amnt = float(input("Enter the amount in Malaysia Ringgit (MYR): "))
    total = amnt * usd
    print("Equivalent amount in US British Pound (GBP): RM", total)

else:
    print("Invalid option! Please re-enter number 1 or 2 or 3.")
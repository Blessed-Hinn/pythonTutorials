# Program to check even or odd
"""digit = int(input("Enter a number: "))

if digit % 2 == 0:
    print("%d is even" % digit)
else:
    print("%d is odd" % digit)
"""

# Leap year calculate

"""year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.\n")
        else:
            print(f"{year} is not a leap year.\n")
    else:
        print(f"{year} is a leap year.\n")
else:
    print(f"{year} is not a leap year.\n")
"""

# Pizza Inn program
print("Welcome to Pizza inn\n")
bill = 0
size = input("Please input pizza size. (Small) (Medium) (Large): ").lower()

if size == "small":
    bill = 100
    pepper = input("Add pepper? (Y) or (N): ").lower()
    if pepper == "y":
        bill = bill + 30
elif size == "medium":
    bill = 200
    pepper = input("Add pepper? (Y) or (N): ").lower()
    if pepper == "y":
        bill = bill + 50
else:
    bill = 300
    pepper = input("Add pepper? (Y) or (N): ").lower()
    if pepper == "y":
        bill = bill + 50

cheese = input("Add Extra cheese? Choose(Y) or (N): ").lower()
if cheese == "y":
    bill = bill + 20

print(f"Total bill is {bill}")
print("Thank you for your order!")

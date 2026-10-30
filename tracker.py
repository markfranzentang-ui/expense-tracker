# Expense Tracker - Installment 4
# Author: Mark Franzen Tang

subtotal: float = 0.0

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)
print("\nWelcome! This is your personal expense tracker.")

print("\nMAIN MENU")
print(" [1] Add an expense\t\t(coming soon)")
print(" [2] View all expenses\t\t(coming soon)")
print(" [3] Show total spent\t\t(coming soon)")
print(" [4] Exit\t\t\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("\nFirst Expense? ")
amount1 = float(input("Amount? "))
if amount1 > 200:
    print("Huge expense - are you sure?")

elif amount1 > 100:
    print("Big expense.")

elif amount1 > 50:
    print("Moderate expense.")

subtotal: float = subtotal + amount1
item2 = input("Second Expense? ")
amount2 = float(input("Amount? "))
if amount2 > 200:
    print("Huge expense - are you sure?")

elif amount2 > 100:
    print("Big expense.")

elif amount2 > 50:
    print("Moderate expense.")

elif amount1 and amount2 > 100:
    print("Two big expenses in a row - slow down!")
subtotal: float = subtotal + amount2
average: float = subtotal / 2

tax_percent: int = int(input("Tax rate? %"))
tax: float = subtotal * (tax_percent / 100)
total: float = subtotal + tax

budget = float(input("Your budget? "))
left = budget - total

print("\n", "-" * 40)
print("SUMMARY")
print(f" - {item1}:\t${amount1}")

print(f" - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand Total:\t${total}")

if total > budget:
    print(f"Over budget by ${total - budget}!")

elif total > budget * 0.90:
    print(f"Careful: Only ${budget - total} left.")

else:
    print(f"Within budget. ${budget - total}")

print("-" * 40)
print("Made by: Mark Franzen Tang | Installment 3")
print("=" * 40)
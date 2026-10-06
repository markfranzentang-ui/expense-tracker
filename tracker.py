# Expense Tracker - Installment 3
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
subtotal: float = subtotal + amount1
item2 = input("Second Expense? ")
amount2 = float(input("Amount? "))
subtotal: float = subtotal + amount2
average: float = subtotal / 2

tax_percent: int = int(input("Tax rate? %"))
tax: float = subtotal * (tax_percent / 100)
total: float = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print("\n", "-" * 40)
print("SUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Budget:\t\t${budget}")
print(f"Over Budget?\t{over_budget}")
print(f"Left in budget:\t$-{left}")
print("-" * 40)
print("Made by: Mark Franzen Tang | Installment 3")
print("=" * 40)
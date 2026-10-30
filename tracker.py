# Expense Tracker - Installment 5
# Author: Mark Franzen Tang

choice = 0
expense : int = 0
subtotal : float = 0
grand_total : float = 0


name = input("\nWhat's your name? ")
tax_percent: int = int(input("Tax rate? %"))
tax : float = 0
budget = float(input("Your budget? "))
left = budget - grand_total
print(f"Welcome, {name}!")


while choice != "4":
   print("\nMAIN MENU")
   print(" [1] Add an expense")
   print(" [2] View all expenses\t\t(coming soon)")
   print(" [3] Show total spent")
   print(" [4] Exit")

   choice = input("Choose 1-4: ")

   if choice == "1":
    expense += 1
    amount = float(input("Amount? "))
    subtotal = subtotal + amount
    tax: float = subtotal * (tax_percent / 100)
    grand_total: float = subtotal + tax

    if amount > 200:
        print("Huge expense - are you sure?")

    elif amount > 100:
        print("Big expense.")

    elif amount > 50:
        print("Moderate expense.")

   elif choice == "2":
       print("Coming soon: the tracker can't remember each item yet.")

   elif choice == "3":
       print(f"Expenses:\t{expense}")
       print(f"Subtotal:\t{subtotal}")
       print(f"Tax({tax_percent}):\t\t{tax}")
       print(f"Grand Total:\t{grand_total}")

       if grand_total > budget:
        print(f"Over budget by ${grand_total - budget}!")

       elif grand_total > budget * 0.90:
        print(f"Careful: Only ${budget - grand_total} left.")

       else:
        print(f"Within budget. ${budget - grand_total}")

   elif choice == "4":
      print(f"Goodbye, {name}")

   else:
    print("Please choose one of the provided choices.")


print("-" * 40)
print("Made by: Mark Franzen Tang | Installment 5")
print("=" * 40)







   











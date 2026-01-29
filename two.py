bill = float(input("Total bill amount? $"))
tip_percent = int(input("Tip percentage (10, 15, 20)? "))
people = int(input("How many people to split the bill? "))

total = bill * (1 + tip_percent / 100)
per_person = total / people

print(f"Each person should pay: ${per_person:.2f}")
# tip calculator

print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? $"))
tip = int(input("What percent of tip would you like to give? 10, 12, or 15? "))
split_bill = int(input("How many people to split the bill? "))
total = ((tip/100)*total_bill+total_bill) / split_bill

print(f"Each person should pay: ${total}")

bill = int(input("What was the total of the bill? "))
tip = int(input("What percentage tip would you like to give? 15, 18, 20? "))
num_people = int(input("How many people are splitting the bill? "))
tip_percent = tip/100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount
bill_per_person = total_bill/num_people
final_amount = round(bill_per_person,2)
print(f"Each person should pay: {final_amount}")

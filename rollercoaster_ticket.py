print("Welcome to the rollercoaster!")
height = int(input("What is your height: "))
bill = 0
if height >= 48:
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("Your ticket is $5")
    elif age >= 18:
        bill = 12
        print("Your ticket is $12")
    else:
        bill = 7
        print("Your ticket is $7")

    wants_photo = input("Do you want a photo taken for $3? Yes or No.")
    if wants_photo == "Yes":
        bill += 3
    print(f"Your total is ${bill}")
else:
    print("Get out of here shorty")
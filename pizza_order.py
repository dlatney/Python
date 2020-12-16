print("Welcome to Python Pizza!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
cheese = 1

if size == "S":
    small_pizza = 15
    if add_pepperoni == "Y":
        pepperoni = 2
        if extra_cheese == "Y":
            total_bill = small_pizza + pepperoni + 1
            print(f"Your total bill is: ${total_bill}")
        else:
            total_bill = small_pizza + pepperoni
            print(f"Your total bill is: ${total_bill}")
    else:
        if extra_cheese == "Y":
            total_bill = small_pizza + 1
            print(f"Your total bill is: ${total_bill}")
        else:
            total_bill == small_pizza
            print(f"Your total bill is: ${total_bill}")
if size == "M":
    small_pizza = 20
    if add_pepperoni == "Y":
        pepperoni = 3
        if extra_cheese == "Y":
            total_bill = small_pizza + pepperoni + 1
            print(f"Your total bill is: ${total_bill}")
        else:
            total_bill = small_pizza + pepperoni
            print(f"Your total bill is: ${total_bill}")
    else:
        if extra_cheese == "Y":
            total_bill = small_pizza + 1
            print(f"Your total bill is: ${total_bill}")
        else:
            total_bill = small_pizza
            print(f"Your total bill is: ${total_bill}")
if size == "L":
    small_pizza = 25
    if add_pepperoni == "Y":
        pepperoni = 3
        if extra_cheese == "Y":
            total_bill = small_pizza + pepperoni + 1
            print(f"Your total bill is: ${total_bill}")
        else:
            total_bill = small_pizza + pepperoni
            print(f"Your total bill is: ${total_bill}")
    else:
        if extra_cheese == "Y":
            total_bill = small_pizza + 1
            print(f"Your total bill is: ${total_bill}")
        else:
            total_bill == small_pizza
            print(f"Your total bill is: ${total_bill}")
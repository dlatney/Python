height = input("Enter your height in inches: ")
weight = input("Enter your weight in pounds: ")

height = int(height)
weight = int(weight)

bmi = ((weight / (height**2))* 703)

print(f"Your BMI is  {bmi}")

message = "Which tells us you're"
if bmi <= 18.5:
    print(f"{message} underweight")
elif bmi <= 25:
    print(f"{message} normal weight")
elif bmi <=30:
    print(f"{message} overweight")
elif bmi <=35:
    print(f"{message} obese")
else:
    print(f"{message} clincally obese")


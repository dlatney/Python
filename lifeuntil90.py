age = input("What is your current age?")
age = int(age)
life = 90 - age
days = 365 * life
weeks = 52 * life
months = 12 * life

print(f"You have {days} days, {weeks} weeks, and {months} months left")
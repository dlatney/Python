print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

combine_names = name1 + name2

t = combine_names.count("t")
r = combine_names.count("r")
u = combine_names.count("u")
e = combine_names.count("e")

true = t + r + u + e

l = combine_names.count("l")
o = combine_names.count("o")
v = combine_names.count("v")
e = combine_names.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
love_score = int(love_score)
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
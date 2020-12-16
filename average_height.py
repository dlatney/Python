student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

numstudent = 0
for student in student_heights:
    numstudent += 1

average = round(total_height / numstudent)
print(student_heights)
print(average)

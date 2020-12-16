list_of_scores = input("Input a list of scores: ").split()
for n in range(0, len(list_of_scores)):

    # list_of_scores[n] = int(list_of_scores[n])
    list_of_scores.sort()
    highest_score = list_of_scores[-1]
print(list_of_scores)
print(highest_score)
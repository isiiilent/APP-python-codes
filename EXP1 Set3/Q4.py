def get_scores():
    n = int(input("Enter the number of students: "))
    scores = []
    for i in range(n):
        score = int(input("Enter the score for student {}: ".format(i+1)))
        scores.append(score)
    return scores

def highest_and_second_highest(scores):
    scores.sort(reverse=True)
    highest = scores[0]
    second_highest = scores[1]
    return highest, second_highest

scores = get_scores()
highest, second_highest = highest_and_second_highest(scores)

print("The highest score is:", highest)
print("The second highest score is:", second_highest)

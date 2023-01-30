num_students = int(input("Enter the number of students: "))
scores = []
for i in range(num_students):
    score = int(input(f"Enter score for student {i + 1}: "))
    scores.append(score)

scores.sort(reverse=True)
print(f"The highest score is {scores[0]}")
print(f"The second highest score is {scores[1]}")
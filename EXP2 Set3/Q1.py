input_string = input('Enter Numbers')
numbers = input_string.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print("Average = ", sum(numbers) / len(numbers))
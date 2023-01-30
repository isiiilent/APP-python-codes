def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

perfect_numbers = [num for num in range(2, 10000) if is_perfect(num)]
print(perfect_numbers[:4])
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def twin_primes(limit):
    twin_primes = []
    for num in range(3, limit, 2):
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

twins = twin_primes(1000)
for twin in twins:
    print(f"({twin[0]}, {twin[1]})")
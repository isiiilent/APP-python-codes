def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def mersenne_primes(limit):
    mersenne_primes = []
    for p in range(2, limit):
        num = 2**p - 1
        if is_prime(num):
            mersenne_primes.append((p, num))
    return mersenne_primes

mersennes = mersenne_primes(62)
for mersenne in mersennes:
    print(f"2^{mersenne[0]} - 1 = {mersenne[1]}")
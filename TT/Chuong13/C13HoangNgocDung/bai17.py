def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(n=100, start=2):
    prime_list = []
    num = start
    while len(prime_list) < n:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    print("The first", n, "prime numbers greater than or equal to", start, "are:", prime_list)

primes(10, 5)


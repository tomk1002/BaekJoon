def sieve(x):
    is_prime = [True] * (x+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(x**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, x+1, i):
                is_prime[j] = False
    return is_prime

def gold_pair(num, is_prime):
    a, b = num // 2, num // 2   # start from the middle
    while a > 1:
        if is_prime[a] and is_prime[b]:
            return f"{a} {b}"
        a -= 1
        b += 1
    return None  # shouldn't happen if Goldbach holds

n = int(input())
for _ in range(n):
    num = int(input())
    primes = sieve(num)
    print(gold_pair(num, primes))
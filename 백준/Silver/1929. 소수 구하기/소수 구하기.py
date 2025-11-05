import sys
input = sys.stdin.readline

N, M = map(int,input().split())

def sieve(n,m):
    isPrime = [True]*(m+1)
    isPrime[0] = isPrime[1] = False

    for i in range(2, int(m**(1/2))+1):
        if isPrime[i]:
            # for j in range(i*i, m+1, i):
            #     isPrime[j] = False
            isPrime[i*i : m+1 : i] = [False]*len(range(i*i, m+1, i))
    return isPrime

primes = sieve(N,M)
for i in range(N,M+1):
    if primes[i]:
        print(i)
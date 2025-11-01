import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

def sieve(num):
    isPrime = [True] * (num+1)
    isPrime[0] = isPrime[1] = False

    for i in range(2,int((num)**0.5)+1):
        if isPrime[i]:
            for j in range(i*i,num+1,i):
                isPrime[j] = False

    return isPrime

isPrime = sieve(max(nums))
count = sum(1 for number in nums if isPrime[number])
print(count)
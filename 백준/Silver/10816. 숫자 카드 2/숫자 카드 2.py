import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

M = int(input())
given = list(map(int,input().split()))


res = [freq.get(x, 0) for x in given]
print(*res)
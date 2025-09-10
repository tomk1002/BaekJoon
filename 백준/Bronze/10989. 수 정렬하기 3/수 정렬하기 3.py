import sys

n = int(input())
nums = [0]*10001

for i in range(n):
    input = sys.stdin.readline
    nums[int(input())] +=1

for i in range(10001):
    for _ in range(nums[i]):
        print(i)
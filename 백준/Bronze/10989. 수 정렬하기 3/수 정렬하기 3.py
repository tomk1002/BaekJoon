import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nums = [0]*10001

for i in range(n):
    nums[int(input())] +=1

for i in range(10001):
    # if nums[i]:
    #     # sys.stdout.write((str(i) + '\n') * nums[i])
    for _ in range(nums[i]):
        print(i)
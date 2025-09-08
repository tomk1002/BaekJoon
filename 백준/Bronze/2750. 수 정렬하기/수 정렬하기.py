n = int(input())
nums = []
for _ in range(n):
    x = int(input())
    nums.append(x)

nums.sort()
for number in nums:
    print(number)
n = int(input())
nums = [0,1]
num = 1
while num <= n:
    nums[0],nums[1] = nums[1],(nums[0]+nums[1])%15746
    num+=1

print(nums[1])
import sys
n = int(sys.stdin.readline())
nums1 = list(map(int,sys.stdin.readline().split()))
k = int(sys.stdin.readline())
nums2 = list(map(int,sys.stdin.readline().split()))
nums1.sort()

for number in nums2:
    left = 0
    right = n-1

    while left <= right:
        mid = (left+right)//2

        if number == nums1[mid]:
            break
        elif number > nums1[mid]:
            left = mid + 1
        else:
            right = mid -1
        
    if number == nums1[mid]:
        print(1)
    else:
        print(0)
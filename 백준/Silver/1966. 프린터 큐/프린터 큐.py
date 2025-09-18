import sys
from collections import deque
test = int(sys.stdin.readline())


for _ in range(test):
    N, M = map(int,sys.stdin.readline().split())
    priority = deque(list(map(int,sys.stdin.readline().rstrip().split())))

    nums = [i for i in range(N)]
    rotation = deque(nums)
    target = nums[M]
    print_count = 0

    while True:
        prior = max(priority)
        pap = priority.popleft()
        s = rotation.popleft()
        if pap < prior:
            priority.append(pap)
            rotation.append(s)
        else:
            print_count += 1
            if s == target:
                break
    print(print_count)



        




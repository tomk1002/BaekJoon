import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    order = input().rstrip()
    M = int(input())
    given = input().rstrip().strip('[]')
    case = deque(given.split(',')) if given else deque()
    
    flipped = False
    escaped = False


    for cmd in order:
        if cmd == 'R':
            flipped = not flipped
        if cmd == 'D':
            if not case:
                escaped = True
                break
            if flipped:
                case.pop()
            else:
                case.popleft()

    if escaped == True:
        print('error')
    else:
        if flipped:
            print(f"[{','.join(map(str,reversed(case)))}]")
        else:
            print(f"[{','.join(map(str,case))}]")
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    order = input().strip()
    M = int(input())
    given = input().strip()

    if M == 0:
        case = deque()
    else:
        case = deque(given[1:-1].split(','))
    
    flipped = False
    error = False

    for cmd in order:
        if cmd == 'R':
            flipped = not flipped
        if cmd == 'D':
            if not case:
                error = True
                break
            if flipped:
                case.pop()
            else:
                case.popleft()

    if error:
        print('error')
    else:
        if flipped:
            case.reverse()
        print(f"[{','.join(case)}]")
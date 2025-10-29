import sys
input = sys.stdin.readline


N = int(input())

que = []
def command(line):
    order = line.split()
    word = order[0]
    if word == 'push':
        que.append(int(order[1]))
    elif word == 'pop':
        if not que:
            print(-1)
        else:
            print(que[0])
            que.remove(que[0])
    elif word == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])
    elif word == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])
    elif word == 'size':
        print(len(que))
    else:
        if que:
            print(0)
        else:
            print(1)


for _ in range(N):
    line = input()
    command(line)


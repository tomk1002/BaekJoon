import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())

lectures = []
for _ in range(N):
    code, start, end = map(int, input().split())
    lectures.append((start, end, code))

# 시작 시간 기준으로 정렬
lectures.sort()

heap = []   # (end_time, room_number)
count = 0
room = [0] * (N+1)

for start, end, code in lectures:
    if heap and heap[0][0] <= start:   # 가장 빨리 끝나는 강의실 재사용 가능
        endtime, room_num = heappop(heap)
        room[code] = room_num
        heappush(heap, (end, room_num))
    else:   # 새로운 강의실 필요
        count += 1
        room[code] = count
        heappush(heap, (end, count))

print(count)
for i in range(1, N+1):
    print(room[i])
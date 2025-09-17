import sys
import heapq
n = int(sys.stdin.readline())

# get home,office x-values
routes_raw = []
for _ in range(n):
    route = list(map(int,sys.stdin.readline().split()))
    routes_raw.append(route)
# get railroad length
rail = int(sys.stdin.readline())
# sort routes ==> shorter than railroads, higher x comes first
routes = []
for route in routes_raw:
    if abs(route[1]-route[0]) <= rail:
        route.sort()
        routes.append(route)
# sort route again => ascending w/ respect to higher x
routes.sort(key=lambda x: x[1])

ans = 0
heap = []
for route in routes:
    if not heap:
        heapq.heappush(heap,route)
    else:
        while heap[0][0] < route[1] - rail:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap,route)
    ans = max(ans,len(heap))

print(ans)

import sys
sys.setrecursionlimit(10**9)
v,e = map(int,input().split())
edges = []

# Vertex값 고려 루트 만들어두기
parent = [i for i in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    # 넣을 때 순서 정리해서 불필요한 lambda 사용 줄이기
    edges.append((c,a,b))
edges.sort()

# 재귀 호출 통한 집합의 루트값 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 루트 일치 여부 확인
def not_union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        # 값이 다를 때 정렬 필요 없이 루트 일치 여부만 리턴
        parent[b] = a
        return True
    return False

total = 0
for cost,a,b in edges:
    if not_union(a,b):
        # 루트 불일치시 가중치 더하기
        total += cost
        
print(total)
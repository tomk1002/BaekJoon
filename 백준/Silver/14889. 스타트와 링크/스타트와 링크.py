import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
players = list(range(N))
min_diff = float('inf')

def team_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            x, y = team[i], team[j]
            score += S[x][y] + S[y][x]
    return score

# 조합 절반만 보기
combs = list(combinations(players, N // 2))
half = len(combs) // 2

for i in range(half):
    team_a = combs[i]
    team_b = combs[-i - 1]  # 반대쪽 조합은 team_b로 간주

    score_a = team_score(team_a)
    score_b = team_score(team_b)
    diff = abs(score_a - score_b)
    min_diff = min(min_diff, diff)

    if min_diff == 0:
        break

print(min_diff)
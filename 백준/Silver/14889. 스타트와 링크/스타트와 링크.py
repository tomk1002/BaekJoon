import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

min_diff = float('inf')
players = list(range(N))

for team_a in combinations(players, N // 2):
    team_b = list(set(players) - set(team_a))

    # 능력치 계산 함수
    def team_score(team):
        score = 0
        for i in range(len(team)):
            for j in range(i + 1, len(team)):
                x, y = team[i], team[j]
                score += S[x][y] + S[y][x]
        return score

    score_a = team_score(team_a)
    score_b = team_score(team_b)
    min_diff = min(min_diff, abs(score_a - score_b))

    if min_diff == 0:
        break  # 더 이상 줄일 수 없음

print(min_diff)
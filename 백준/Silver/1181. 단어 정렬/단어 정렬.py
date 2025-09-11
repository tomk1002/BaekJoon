import sys

n = int(input())
words = []
for i in range(n):
    word = input()
    if word not in words:
        words.append(word)

words.sort()

buckets = [[] for _ in range(51)]

# 길이 기준으로 버킷에 넣기
for word in words:
    buckets[len(word)].append(word)

# 길이가 짧은 것부터 출력
for bucket in buckets:
    for word in bucket:
        print(word)
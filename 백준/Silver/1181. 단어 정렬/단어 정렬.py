import sys

n = int(input())
words = set()

for i in range(n):
    words.add(sys.stdin.readline().strip())

words_by_alph = sorted(words)
words_by_len = sorted(words_by_alph, key=len)

for word in words_by_len:
    print(word)
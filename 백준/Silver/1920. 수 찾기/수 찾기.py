import sys
import bisect

N = int(input())
numbers = list(map(int,sys.stdin.readline().split()))
numbers.sort()

M = int(input())
given = list(map(int,sys.stdin.readline().split()))

for number in given:
    idx = bisect.bisect_left(numbers,number)
    print(int(idx < N and numbers[idx] == number))
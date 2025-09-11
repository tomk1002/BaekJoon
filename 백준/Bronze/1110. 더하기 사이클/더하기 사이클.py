n = int(input())
flag = n
count = 0

first = n%10
temp = n//10 + n%10
second = first*10 + temp%10
count+=1

while flag!= second:
    first = second%10
    temp = second//10 + second%10
    second = first*10 + temp%10
    count+=1

print(count)
parts = input().split('-')

result = sum(map(int,parts[0].split('+')))

for i in parts[1:]:
    tmp = sum(map(int, i.split('+')))
    result -= tmp

print(result)
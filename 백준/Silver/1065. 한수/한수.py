def hansu():
    n = int(input())
    count = 0

    if n < 100:
        count = n
        return count
    else:
        count+=99

    for i in range(100,n+1):
        num = str(i)
        if int(num[2])-int(num[1]) == int(num[1])-int(num[0]):
            count+=1

    return count


print(hansu())
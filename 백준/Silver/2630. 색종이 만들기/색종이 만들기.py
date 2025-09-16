def cut_paper(n,x,y):
    color = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != paper[i][j]:
                d = n//2
                #1,2,3,4 사분면 순서대로
                cut_paper(d,x+d,y)
                cut_paper(d,x,y)
                cut_paper(d,x,y+d)
                cut_paper(d,x+d,y+d)
                return
    if color == 0:
        wb[0] +=1
    else:
        wb[1] +=1

n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
wb = [0,0]
cut_paper(n,0,0)
print(*wb,sep='\n')
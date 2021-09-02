import sys
input = sys.stdin.readline

def width(x1,y1,x2,y2,x3,y3):
    ans = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2
    return ans

orc = [list(map(int,input().split())) for _ in range(3)]*2
N = int(input())
apple = [list(map(int,input().split())) for _ in range(N)]
tot, cnt = width(orc[0][0],orc[0][1],orc[1][0],orc[1][1],orc[2][0],orc[2][1]), 0
for i in apple:
    a = width(i[0],i[1],orc[1][0],orc[1][1],orc[2][0],orc[2][1])
    b = width(orc[0][0],orc[0][1],orc[1][0],orc[1][1],i[0],i[1])
    c = width(orc[0][0],orc[0][1],i[0],i[1],orc[2][0],orc[2][1])
    if a+b+c == tot:
        cnt += 1
print(tot)
print(cnt)
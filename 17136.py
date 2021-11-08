import sys
input = sys.stdin.readline

def check(x,y,cnt):
    global ans
    if y >= 10:
        ans = min(ans, cnt)
        return 0
    if x >= 10:
        check(0,y+1,cnt)
        return 0
    if pan[x][y] == 1:
        for i in range(5):
            flag = True
            if arr[i] == 5 or x+i >= 10 or y+i >= 10:
                continue
            for j in range(x,x+i+1):
                for k in range(y,y+i+1):
                    if pan[j][k] == 0:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                for j in range(x,x+i+1):
                    for k in range(y,y+i+1):
                        pan[j][k] = 0
                arr[i] += 1
                check(x+i+1,y,cnt+1)
                arr[i] -= 1
                for j in range(x,x+i+1):
                    for k in range(y,y+i+1):
                        pan[j][k] = 1
    else:
        check(x+1,y,cnt)
                
ans = 100
pan = [list(map(int,input().split())) for _ in range(10)]
arr = [0,0,0,0,0]
check(0,0,0)
if ans != 100:
    print(ans)
else:
    print(-1)
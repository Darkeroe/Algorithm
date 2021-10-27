import sys
input = sys.stdin.readline

def check(x,y,ny,row,column,direction):
    res1,res2 = float('inf'), 0
    if x in row:
        tmp = row[x]
        if y > ny:
            tmp.append((ny,y))
        else:
            tmp.append((y,ny))
        row[x] = tmp
    else:
        if y > ny:
            row[x] = [(ny,y)]
        else:
            row[x] = [(y,ny)]
    for i in column:
        if y+1<=i<ny+1 or ny-1<i<=y-1:
            for j in column[i]:
                if j[0] <= x <= j[1]:
                    res1 = min(res1,i)
                    res2 = max(res2,i)
    if res1 != float('inf') or res2 != 0:
        if direction > 0:
            return res1-y
        else:
            return y-res2
    else:
        return -1

L = int(input())
N = int(input())
row, column = {}, {}
column[L] = [(L,L)]
x,y,dx,dy,cnt,size = L,L,0,1,0,2*L+1
for i in range(N+1):
    if i != N:
        t, LR = map(str,input().split())
    else:
        t, LR = size, 'R'
    nx = x + dx*int(t)
    ny = y + dy*int(t)
    if dx == 0:
        ans = check(x,y,ny,row,column,dy)
    else:
        ans = check(y,x,nx,column,row,dx)
    if ans != -1:
        print(cnt+ans)
        break
    else:
        if nx < 0 :print(cnt+x+1); break
        elif ny < 0 :print(cnt+y+1); break
        elif nx >= size :print(cnt+size-x); break
        elif ny >= size :print(cnt+size-y); break
        x,y = nx,ny
        cnt += int(t)
        if LR == 'R':
            if dx == 0:
                dx,dy = dy,dx
            else:
                dy,dx = -dx,0
        else:
            if dx != 0:
                dx,dy = dy,dx
            else:
                dx,dy = -dy,0
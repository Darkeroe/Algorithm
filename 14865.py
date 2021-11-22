import sys
input = sys.stdin.readline

ans = [1,1]
N = int(input())
vertex = [list(map(int,input().split())) for _ in range(N)]
idx = 0
for i in range(N):
    if vertex[i][0] == vertex[i+1][0] and vertex[i][1] < vertex[i+1][1]:
        idx = i
        tmp = vertex[:i]
        vertex += tmp
        break
    
vertex.append(vertex[idx])
cross_dot = []
flag = False
for i in range(idx+2,idx+N+1,2):
    print('i: ',i)
    x1,y1 = vertex[i-2]
    x2,y2 = vertex[i]
    if flag:
        if (y1<0 and y2>0) or (y1>0 and y2<0):
            cross_dot.append([min(tmp,x1),max(tmp,x1)])
            flag = False
    else:
        if (y1<0 and y2>0) or (y1>0 and y2<0):
            tmp = x1
            flag = True

cross_dot.sort()
right1, right2 = cross_dot[0][1], cross_dot[0][1]
for peak in cross_dot[1:]:
    start,end = peak[0],peak[1]
    if right1 < start:
        right1,right2 = end,end
        ans[0] += 1
        ans[1] += 1
    else:
        if right1 > start > right2:
            ans[1] += 1
            right2 = end
        elif start < right2:
            right2 = end

print(*ans)
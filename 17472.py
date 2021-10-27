from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
canvas = [list(map(int,input().split())) for _ in range(N)]
row = [[] for _ in range(N)]
column = [[] for _ in range(M)]
bridge = []

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def bfs(x,y,num):
    queue = deque()
    queue.append([x,y])
    canvas[x][y] = num
    while queue:
        x,y = queue.pop()
        row[x].append([y,num])
        column[y].append([x,num])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and canvas[nx][ny] == 1:
                canvas[nx][ny] = num
                queue.append([nx,ny])

def connect(arr):
    for i in arr:
        i.sort()
        for j in range(len(i)-1):
            if i[j+1][1] != i[j][1] and i[j+1][0]-i[j][0]-1 >= 2:
                bridge.append([i[j+1][0]-i[j][0]-1,i[j+1][1]-1,i[j][1]-1])

def union(a, b):
    a = find(a)
    b = find(b)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

cnt,ans = 2,0
for i in range(N):
    for j in range(M):
        if canvas[i][j] == 1:
            bfs(i,j,cnt)
            cnt += 1

connect(row)
connect(column)
bridge.sort()
parent = list(range(cnt-1))

cnt2 = 0
for w, s, e in bridge:
    if find(s) != find(e):
        union(s, e)
        cnt2 += 1
        ans += w
        
if ans == 0 or cnt2 < cnt-3:
    print(-1)
else:
    print(ans)
import math
from collections import deque

def bfs(fuel,fill):
    queue = deque()
    queue.append([0,0,0,fill])
    visited = [[0] for _ in range(n+1)]
    visited[0] = 1
    while queue:
        x, y, z, fill = queue.popleft()
        for i in range(1,n+1):
            if i != z and dist[i][z] == 0:
                dist[i][z] = dist[z][i] = math.sqrt(pow(airfield[i][0]-airfield[z][0], 2) + pow(airfield[i][1]-airfield[z][1], 2))
            if i != z and visited[i] != 1 and  dist[i][z] <= fuel*10:
                if fill - 1 < 0:
                    return False
                if dist [i][n+1] == 0:
                    dist[i][n+1] = math.sqrt(pow(airfield[i][0]-airfield[n+1][0], 2) + pow(airfield[i][1]-airfield[n+1][1], 2))
                if dist[i][n+1] <= fuel*10:
                    return True
                queue.append(airfield[i]+[fill-1])
                visited[i] = 1
    return False

n,k = map(int,input().split())
airfield = [[0,0,0]]
for i in range(n):
    airfield.append(list(map(int,input().split())))
    airfield[i+1].append(i+1)
airfield.append([10000,10000,n+1])
dist = [[0 for _ in range(n+2)] for _ in range(n+2)]

if k == 0:
    print(1415)
else:
    start, end = 0, 1415
    while start <= end:
        fuel = (start + end)//2
        if bfs(fuel,k):
            res = fuel
            end = fuel - 1
        else:
            start = fuel + 1
    print(res)
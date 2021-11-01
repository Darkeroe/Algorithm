from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [-1,1,0,0]

N,M = map(int,input().split())
room = [[0 for _ in range(N)] for _ in range(N)]
switch = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x,y,a,b = map(int,input().split())
    switch[x-1][y-1].append((a-1,b-1))

cnt = 1
queue = deque()
queue.append([0,0])
room[0][0] = -1
while queue:
    x,y = queue.pop()
    for i in switch[x][y]:
        if room[i[0]][i[1]] != -1:
            if room[i[0]][i[1]] == 3:
                room[i[0]][i[1]] = -1
                queue.append([i[0],i[1]])
                cnt += 1
            else:
                if room[i[0]][i[1]] == 0:
                    cnt += 1
                room[i[0]][i[1]] = 2
                
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and room[nx][ny] != -1:
            if room[nx][ny] == 2:
                room[nx][ny] = -1
                queue.append([nx,ny])
            else:
                room[nx][ny] = 3 
print(cnt)
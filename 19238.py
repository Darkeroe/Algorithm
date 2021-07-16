from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,fuel,state):
    global m
    order = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    queue = deque()
    queue.append([x,y,fuel])

    if space[x][y] >= 2:
        state = space[x][y]
        space[x][y] = 0

    while queue:
        x,y,z = queue.popleft()
        if order != [] and order[0][2] == z:
            order.sort()
            space[order[0][0]][order[0][1]] = 0
            bfs(order[0][0],order[0][1],order[0][2],order[0][3])
            return 0

        if z <= 0:
            return 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if state == 0:
                    if space[nx][ny] >= 2 and visited[nx][ny] != 1:
                        tmp = space[nx][ny]
                        order.append([nx,ny,z-1,tmp])
                        queue.append([nx,ny,z-1])
                        visited[nx][ny] = 1
                    elif space[nx][ny] != 1 and visited[nx][ny] != 1:
                        queue.append([nx,ny,z-1])
                        visited[nx][ny] = 1
                else:
                    if dest[state] == [nx,ny]:
                        m -= 1
                        if m == 0:
                            print(2*fuel-z+1)
                            return 0
                        bfs(nx,ny,2*fuel-z+1,0)
                        return 0
                    elif space[nx][ny] != 1 and visited[nx][ny] != 1:
                        queue.append([nx,ny,z-1])
                        visited[nx][ny] = 1

n, m, fuel = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(n)]
start_x, start_y = map(int,input().split())
customer = [list(map(int,input().split())) for _ in range(m)]
number, ride, dest = 2, 0,  [[0,0]for _ in range(m+2)]
for i in customer:
    space[i[0]-1][i[1]-1] = number
    dest[number] = [i[2]-1,i[3]-1]
    number += 1
bfs(start_x-1,start_y-1,fuel,ride)
if m != 0:
    print(-1)
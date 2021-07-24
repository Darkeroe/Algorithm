from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def start(w,h):
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                building[i][j] = '.'
                x,y = i,j
            elif building[i][j] == '*':
                fire.append([i,j,1])
    fire.append([x,y,0])

def bfs(w,h):
    cnt, flag = 0, True
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    while fire:
        x,y,z = fire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if building[nx][ny] != '#' and building[nx][ny] != '*':
                    if z == 1 :
                        building[nx][ny] = '*'
                        fire.append([nx,ny,1])
                    else:
                        flag = False
                        if visited[x][y] == -1:
                            visited[x][y] = 0
                        if visited[nx][ny] == -1:
                            fire.append([nx,ny,0])
                            visited[nx][ny] = visited[x][y] + 1
            else:
                if z == 0:
                    if flag== True:
                        print(1)
                    else:
                        print(visited[x][y]+1)
                    return cnt
    print('IMPOSSIBLE')
    
test = int(input())
for i in range(test):
    w, h = map(int,input().split())
    building = [list(str(input())) for _ in range(h)]
    fire = deque()
    start(w,h)
    bfs(w,h)

from collections import deque

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def bfs(arr):
    res = 0
    queue = deque()
    for i in arr:
        x, y = i[0], i[1]
        queue.append([x,y])
        while queue:
            x, y = queue.popleft()
            if field[x][y] == 1:
                res += 1
            field[x][y] = -1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N and field[nx][ny] == 1:
                    queue.append([nx,ny])
                    field[nx][ny] = -1
    print(res)

T = int(input())
for _ in range(T):
    M, N, K = map(int,input().split())
    field = [[0 for _ in range(N)] for _ in range(M)]
    arr = []
    for _ in range(K):
        x, y = map(int,input().split())
        field[x][y] = 1
        arr.append([x,y])
    bfs(arr)
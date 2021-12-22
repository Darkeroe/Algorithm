import sys
from collections import deque

input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def check_intersection():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                flag = -1
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1:
                        if flag == -1:
                            flag = k
                        elif k - flag == 1 or k - flag == 3:
                            board[i][j] = -1
                            break


def bfs(start_x, start_y):
    ans = float("inf")
    queue = deque()
    queue.append([0, start_x, start_y, 0, 0])
    while queue:
        t, x, y, use_bridge, pri_bridge = queue.pop()
        if x == N - 1 and y == N - 1:
            ans = min(ans, t)
            continue
        if use_bridge == 1:
            visited[x][y][1] = t
        else:
            visited[x][y][0] = t
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == -1:
                    continue
                elif board[nx][ny] == 0:
                    if use_bridge != 1:
                        tmp = M
                        while tmp <= t:
                            tmp += M
                        if tmp < visited[nx][ny][0] and pri_bridge == 0:
                            queue.append([tmp, nx, ny, 1, 1])
                elif board[nx][ny] == 1:
                    if (use_bridge == 0 and t < visited[nx][ny][0]) or (
                        use_bridge == 1 and t < visited[nx][ny][1]
                    ):
                        queue.append([t + 1, nx, ny, use_bridge, 0])
                else:
                    tmp = board[nx][ny]
                    while tmp <= t:
                        tmp += board[nx][ny]
                    if (use_bridge == 0 and tmp < visited[nx][ny][0]) or (
                        use_bridge == 1 and tmp < visited[nx][ny][1]
                    ):
                        if pri_bridge != 1:
                            queue.append([tmp, nx, ny, use_bridge, 1])
    return ans


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[[float("inf"), float("inf")] for _ in range(N)] for _ in range(N)]
check_intersection()
print(bfs(0, 0))

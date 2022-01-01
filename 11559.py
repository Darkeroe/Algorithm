import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def down():
    for i in range(6):
        for j in range(12):
            if field[11 - j][i] != ".":
                for k in range(j):
                    if field[11 - k][i] == ".":
                        field[11 - k][i] = field[11 - j][i]
                        field[11 - j][i] = "."
                        break


def boom(arr):
    for x, y in arr:
        field[x][y] = "."


def bfs(x, y):
    flag = False
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    linked = [[x, y]]
    while queue:
        x, y = queue.pop()
        color = field[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < 12
                and 0 <= ny < 6
                and visited[nx][ny] == 0
                and field[nx][ny] == color
            ):
                queue.append([nx, ny])
                visited[nx][ny] = 1
                linked.append([nx, ny])
    if len(linked) >= 4:
        boom(linked)
        flag = True
    return flag


def go():
    global ans, visited
    ans += 1
    flag = False
    for i in range(12):
        for j in range(6):
            if visited[i][j] == 0 and field[i][j] != "." and bfs(i, j):
                flag = True
    if flag:
        visited = [[0 for _ in range(6)] for _ in range(12)]
        down()
        go()
    else:
        return 0


ans = -1
field = [list(input().rstrip()) for _ in range(12)]
visited = [[0 for _ in range(6)] for _ in range(12)]
go()

print(ans)

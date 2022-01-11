import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    queue.append((0, 0, 1))
    maze[0][0] = 0

    while queue:
        x, y, cnt = queue.popleft()

        if x == n - 1 and y == m - 1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = 0
                queue.append((nx, ny, cnt + 1))

    return 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = [list(map(int, input().rstrip())) for _ in range(n)]
    ans = bfs()
    print(ans)

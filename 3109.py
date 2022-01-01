import sys

input = sys.stdin.readline

dx = [-1, 0, 1]


def dfs(x, y):
    visited[x][y] = 1
    if y == C - 1:
        return True
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        if (
            0 <= nx < R
            and field[nx][ny] == "."
            and visited[nx][ny] == 0
            and dfs(nx, ny)
        ):
            return True
    return False


ans = 0
R, C = map(int, input().split())
field = [list(input().rstrip()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    if field[i][0] == "." and dfs(i, 0):
        ans += 1
print(ans)

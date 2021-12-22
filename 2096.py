import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp1 = [[0, 0, 0] for _ in range(2)]
dp2 = [[0, 0, 0] for _ in range(2)]
dp1[0] = board[0][:]
dp2[0] = board[0][:]

for i in range(1, N):
    if i % 2 == 1:
        pri, x = 0, 1
    else:
        pri, x = 1, 0
    for j in range(3):
        if j == 0:
            dp1[x][j] = max(dp1[pri][j], dp1[pri][j + 1]) + board[i][j]
            dp2[x][j] = min(dp2[pri][j], dp2[pri][j + 1]) + board[i][j]
        elif j == 1:
            dp1[x][j] = max(dp1[pri][j - 1], dp1[pri][j], dp1[pri][j + 1]) + board[i][j]
            dp2[x][j] = min(dp2[pri][j - 1], dp2[pri][j], dp2[pri][j + 1]) + board[i][j]
        else:
            dp1[x][j] = max(dp1[pri][j - 1], dp1[pri][j]) + board[i][j]
            dp2[x][j] = min(dp2[pri][j - 1], dp2[pri][j]) + board[i][j]

if N % 2 == 1:
    print(max(dp1[0]), min(dp2[0]))
else:
    print(max(dp1[1]), min(dp2[1]))

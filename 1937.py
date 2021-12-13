import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def dfs(x,y):
    if not dp[x][y]:
        dp[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and forest[x][y] < forest[nx][ny]:
                dp[x][y] = max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]

ans = 0
n = int(input())
forest = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        ans = max(ans,dfs(i,j))
print(ans)
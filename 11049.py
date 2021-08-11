N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[float('inf') for _ in range(N)] for _ in range(N)]

for i in range(N+1):
    for j in range(N-i):
        if i == 0:
            dp[j][j] = 0
        else:
            for k in range(j,j+i):
                dp[j][j+i] = min(dp[j][j+i],dp[j][k]+ dp[k+1][j+i] + arr[j][0]*arr[k][1]*arr[j+i][1])

print(dp[0][N-1])
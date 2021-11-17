import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
dp[1][0] = 1
for i in range(2,N+1):
    for j in range(i):
        if i & 1:
            for k in range(j,i):
                dp[i][j] += dp[i-1][k]
        else:
            for k in range(0,j):
                dp[i][j] += dp[i-1][k]

ans = [0 for _ in range(N)]
ans[0] = 1

for i in range(2,N+1):
    for j in range(i):
        ans[i-1] += dp[i][j]
    ans[i-1] *= 2

print(ans[N-1]%1000000)
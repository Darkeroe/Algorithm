import sys
input = sys.stdin.readline

T = int(input())
dp = [[0 for _ in range(21)] for _ in range(21)]
dp[1][0] = 1
for i in range(2,21):
    for j in range(i):
        if i & 1:
            for k in range(j,i):
                dp[i][j] += dp[i-1][k]
        else:
            for k in range(0,j):
                dp[i][j] += dp[i-1][k]
                
ans = [0 for _ in range(20)]
ans[0] = 1

for i in range(2,21):
    for j in range(i):
        ans[i-1] += dp[i][j]
    ans[i-1] *= 2

for i in dp:
    print(i)
    print()
print(ans)

for _ in range(T):
    N = int(input())
    print(ans[N-1])

import sys
input = sys.stdin.readline

N = int(input())
rock = [list(map(int,input().split())) for _ in range(N-1)]
K = int(input())

dp = [[0,float('inf')] for _ in range(N)]
if rock:
    dp[1][0] = rock[0][0]
    for i in range(2,N):
        tmp1, tmp2, ans = 0, float('inf'), 0
        for j in range(i-1):
            if j == 0:
                dp[i][0] = min(dp[i-1][0] + rock[i-1][0], dp[i-2][0]+rock[i-2][1])
            else:
                if j > 1:                    
                    ans = min(tmp1+rock[i-j+1][0],tmp2+rock[i-j+1][1])
                    tmp2, tmp1 = tmp1, ans
                dp[i][1] = min(dp[i][1], dp[i-3-j+1][0]+ K + ans)
print(min(dp[N-1]))
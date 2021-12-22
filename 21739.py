import sys

input = sys.stdin.readline
mod = 10 ** 9 + 7


N = int(input())
dp = [0 for _ in range(N + 1)]
dp[0] = 1
for i in range(1, N + 1):
    for j in range(i):
        dp[i] = (dp[i] + dp[j] * dp[i - j - 1] % mod) % mod

print(dp[-1])
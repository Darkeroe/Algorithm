import sys

input = sys.stdin.readline
mod = 9901


def calc():
    for i in range(2, a + 1):
        dp[i] = (2 * (dp[i - 1]) + dp[i - 2]) % mod
    return dp[a]


if __name__ == "__main__":
    a = int(input())
    dp = [1 for _ in range((a + 1) * 2)]
    dp[1] = 3
    print(calc())

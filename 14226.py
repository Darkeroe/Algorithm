from collections import deque
import sys
input = sys.stdin.readline

S = int(input())
dp = [[-1 for _ in range(S+1)] for _ in range(S+1)]
dp[1][0] = 0
queue = deque()
queue.append([1,0])
while queue:
    screen, clipboard = queue.popleft()
    if dp[screen][screen] == -1:
        dp[screen][screen] = dp[screen][clipboard]+1
        queue.append([screen,screen])
    if screen+clipboard <= S and dp[screen+clipboard][clipboard] == -1:
        dp[screen+clipboard][clipboard] = dp[screen][clipboard] + 1
        queue.append((screen+clipboard, clipboard))
    if screen-1 >= 0 and dp[screen-1][clipboard] == -1:
        dp[screen-1][clipboard] = dp[screen][clipboard] + 1
        queue.append((screen-1, clipboard))
ans = -1
for i in range(S):
    if dp[S][i] != -1 and (ans == -1 or ans > dp[S][i]):
            ans = dp[S][i]
print(ans)
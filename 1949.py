from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

def dfs(node):
    visited[node] = 1
    for i in tree[node]:
        if not visited[i]:
            dfs(i)
            dp[node][0] += dp[i][1]
            dp[node][1] += max(dp[i][0],dp[i][1])

N = int(input())
citizen = [0] + list(map(int,input().split()))
visited = [0 for _ in range(N+1)]
dp = [[citizen[i],0] for i in range(N+1)]
tree = defaultdict(list)
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)

print(max(dp[1][0],dp[1][1]))
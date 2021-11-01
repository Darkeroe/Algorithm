from itertools import permutations
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
cost = [[float('inf') for _ in range(N)] for _ in range(N)]
for i in range(N):
    cost[i] = list(map(int,input().split()))

for k in range(N):
    for a in range(N):
        for b in range(N):
            cost[a][b] = min(cost[a][b], cost[a][k] + cost[k][b])

items = []
for i in range(N):
    if i != K:
        items.append(i)
arr = list(permutations(items,N-1))
ans = float('inf')

for i in arr:
    tmp,start = 0,K
    for j in i:
        tmp += cost[start][j]
        start = j
        if tmp >= ans:
            break
    ans = min(ans,tmp)
print(ans)
from heapq import heappush,heappop
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    tmp = list(map(int,input().split()))
    heappush(heap,tmp)

ans = []
for i in range(N):
    tmp = heappop(heap)
    heappush(ans,tmp[1])
    if tmp[0] < len(ans):
        heappop(ans)

print(sum(ans))
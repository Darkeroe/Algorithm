import sys
import heapq

N, K = map(int,sys.stdin.readline().split())
jewel = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
jewel = sorted(jewel,key = lambda x : -x[0])
bag = [int(sys.stdin.readline()) for _ in range(K)]
bag.sort()
heap,ans = [],0
for i in bag:
    for j in range(N-1,-1,-1):
        if jewel[j][0] <= i:
            heapq.heappush(heap,-jewel[j][1])
            N -= 1
        else:
            break
    if len(heap) != 0:
        ans += -heapq.heappop(heap)
print(ans)
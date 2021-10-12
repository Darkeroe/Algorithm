import heapq
import sys
input = sys.stdin.readline

N = int(input())
min_heap,max_heap = [], []
for _ in range(N):
    tmp = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap,-tmp)
    else:
        heapq.heappush(min_heap,tmp)
    if min_heap and -1*max_heap[0] > min_heap[0]:
        a = heapq.heappop(max_heap)
        b = heapq.heappop(min_heap)
        heapq.heappush(max_heap,-b)
        heapq.heappush(min_heap,-a)
    print(-1*max_heap[0])
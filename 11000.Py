import heapq
heap = []

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort()

heapq.heappush(heap, arr[0][1])

for i in arr[1:]:
    if heap[0] > i[0]:
        heapq.heappush(heap,i[1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap,i[1])

print(len(heap))
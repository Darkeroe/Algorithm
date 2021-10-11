import heapq
import sys
input = sys.stdin.readline

N,P,T = map(int,input().split())
rock = list(map(int,input().split()))
arr = [[-rock[0],0] for _ in range(N)]
for i in range(1,N):
    arr[i] = [-1*(rock[i]+T),i]
heap = []
for i in range(N):
    P -= -1*arr[i][0]
    heapq.heappush(heap,arr[i])
    if P < 0:
        a,b = heapq.heappop(heap)
        P += -1*a -T
        if b == 0:
            P += T
print(len(heap))
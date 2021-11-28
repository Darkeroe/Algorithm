from heapq import heappush,heappop
from collections import defaultdict
import sys
input = sys.stdin.readline

def dijkstra(start,road):
    queue = []
    visited = [0 for _ in range(N)]
    distance[start] = 0
    heappush(queue, [0, start])
    
    while queue:
        current_distance, current_node = heappop(queue)
        
        if visited[current_node] == 1 and distance[current_node] <= current_distance: continue
        visited[current_node] = 1
        
        for i in road[current_node]:
            if distance[i] > current_distance + road[current_node][i]:
                distance[i] = current_distance + road[current_node][i]
                heappush(queue, [distance[i],i])

    return distance

N,M,X = map(int,input().split())
road = defaultdict(dict)
road_reverse = defaultdict(dict)
for _ in range(M):
    start,end,cost = map(int,input().split())
    road[start-1][end-1] = cost
    road_reverse[end-1][start-1] = cost

ans = [0 for _ in range(N)]
for i in range(2):
    distance = [float('inf') for _ in range(N)]
    if i == 0: 
        ans = dijkstra(X-1,road)
    else: 
        ans = [x+y for x,y in zip(ans,dijkstra(X-1,road_reverse))]

print(max(ans))
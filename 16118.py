import heapq
import sys
input = sys.stdin.readline

def find():
    dist = [float('inf') for _ in range(N)]
    dist[0],heap = 0,[]
    heapq.heappush(heap,[0,1])
    cnt = N-1
    while heap and cnt:
        acc, prev = heapq.heappop(heap)
        if dist[prev-1] < acc:
            continue
        for node, length in road[prev]:
            if dist[node-1] > acc + length:
                dist[node-1] = acc + length
                heapq.heappush(heap, [acc+length,node])
        cnt -= 1
    return dist

def find2():
    dist = [[float('inf'),float('inf')] for _ in range(N)]
    dist[0][1],heap = 0,[]
    heapq.heappush(heap,[0,1,True])
    cnt = 2*N-1
    while heap and cnt:
        acc, prev, flag = heapq.heappop(heap)
        if flag and dist[prev-1][1] < acc:
            continue
        elif not flag and dist[prev-1][0] < acc:
            continue

        for node,length in road[prev]:
            if flag:
                tmp = acc + length//2
                if dist[node-1][0] > tmp:
                    dist[node-1][0] = tmp
                    heapq.heappush(heap,[tmp,node,False])
            else:
                tmp = acc + length*2
                if dist[node-1][1] > tmp:
                    dist[node-1][1] = tmp
                    heapq.heappush(heap,[tmp,node,True])
        cnt -= 1
    return dist

N,M = map(int,input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    road[a].append([b,c*2])
    road[b].append([a,c*2])
dist,dist2,ans = find(),find2(),0
for i in range(1, N):
    if dist[i] < dist2[i][0] and dist[i] < dist2[i][1]:
        ans += 1
print(ans)
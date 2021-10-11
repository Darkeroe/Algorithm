import heapq
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    heap = []
    heapq.heappush(heap,[maze[0][0],0,0])
    rupee = [[float('inf') for _ in range(N)] for _ in range(N)]
    rupee[0][0] = maze[0][0]
    while heap:
        gold,x,y = heapq.heappop(heap)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and rupee[nx][ny] > gold + maze[nx][ny]:
                rupee[nx][ny] = gold + maze[nx][ny]
                if not (nx == N-1 and ny == N-1):
                    heapq.heappush(heap,[rupee[nx][ny],nx,ny])
                else:
                    return rupee[N-1][N-1]

cnt = 0
while True:
    cnt += 1
    N = int(input())
    if N == 0:break
    maze = [list(map(int,input().split())) for _ in range(N)]
    print('Problem %d: %d'%(cnt,bfs()))
from heapq import heappop,heappush
import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def bfs():
    queue = []
    heappush(queue,[1,0,0])
    visited[0][0] = 1
    while queue:
        cnt,x,y = heappop(queue)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] > cnt:
                if nx == M-1 and ny == N-1:
                    return cnt-1
                if maze[nx][ny] == 0:
                    visited[nx][ny] = cnt
                    heappush(queue,[cnt,nx,ny])
                else:
                    if not visited[nx][ny] == cnt+1:
                        visited[nx][ny] = cnt+1
                        heappush(queue,[cnt+1,nx,ny])
                
N,M = map(int,input().split())
maze = [list(map(int,input().rstrip())) for _ in range(M)]
visited = [[float('inf') for _ in range(N)] for _ in range(M)]
if N == 1 and M == 1:
    print(0)
else:
    print(bfs())
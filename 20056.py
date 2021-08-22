from collections import deque

N,M,K = map(int,input().split())
fire = deque()
for _ in range(M):
    fire.append(list(map(int,input().split()))) 
    # r,c , 질량, 속력, 방향
print(fire)

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
for i in range(K):
    field = [[[0,0,0,0,0] for _ in range(N)] for _ in range(N)]
    tmp = []
    while fire:
        x,y,m,s,d = fire.popleft()
        nx = x-1 + s*dx[d]
        ny = y-1 + s*dy[d]
        if nx >= N:
            nx -= N
        elif nx < 0:
            nx += N
        if ny >= N:
            ny -= N
        elif ny < 0:
            ny += N
        if field[nx][ny][m] == 0:
            field[nx][ny] = [nx+1,ny+1,m,s,d]
        else:
            field[nx][ny][2] += m
            field[nx][ny][3] += s
            if field[nx][ny][4]%2 == 1:
                if d%2 == 1 and d >= 0:
                    field[nx][ny][4] += 10
                else:
                    field[nx][ny][4] 
            else:
        tmp.append([nx+1,ny+1])
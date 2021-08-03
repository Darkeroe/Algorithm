dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
N, M  = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(N)]
cloud = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
ans = 0
for i in range(M):
    d, s = map(int,input().split())
    s %= N
    tmp = 0
    for j in cloud:
        nx = j[0] + dx[d-1]*s
        ny = j[1] + dy[d-1]*s
        if nx < 0:
            nx += N
        elif nx >= N:
            nx -= N
        if ny < 0:
            ny += N
        elif ny >= N:
            ny -= N
        field[nx][ny] += 1
        cloud[tmp] = [nx,ny]
        tmp += 1
    for j in cloud:
        tmp = 0
        for k in range(4):
            nx = j[0] + dx[k*2+1]
            ny = j[1] + dy[k*2+1]
            if 0 <= nx < N and 0 <= ny < N and abs(field[nx][ny]) > 0:
                tmp += 1
        field[j[0]][j[1]] += tmp
        field[j[0]][j[1]] *= -1
    cloud = []
    for j in range(N):
        for k in range(N):
            if field[j][k] >= 2:
                field[j][k] -= 2
                cloud.append([j,k])
            elif field[j][k] < 0:
                field[j][k] *= -1
            if i == M-1:
                ans += field[j][k]
print(ans)
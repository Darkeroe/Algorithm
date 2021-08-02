import math

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def scatter(x,y,p):
    global ans
    p = math.floor(p)
    if 0 <= x < N and 0 <= y < N:
        field[x][y] += p
    else:
        ans += p

def tornado(x,y,i):
    nx = x + dx[i]
    ny = y + dy[i]
    dust = field[nx][ny]
    dust_after = field[nx][ny]
    field[nx][ny] = 0
    for j in range(4):
        if j == i:
            nnx = nx + 2*dx[j]
            nny = ny + 2*dy[j]
            percentage = 0.05
            scatter(nnx,nny,dust*percentage)
            dust_after -= math.floor(dust*percentage)
        elif j != i+2 and j != i-2:
            for k in range(1,3):
                nnx = nx + dx[j]*k
                nny = ny + dy[j]*k
                if k == 1:
                    percentage = 0.07
                else:
                    percentage = 0.02
                scatter(nnx,nny,dust*percentage)
                dust_after -= math.floor(dust*percentage)
            if dx[i] == 0:
                for l in [1,-1]:
                    nnx = nx + dx[j]
                    nny = ny + l
                    if l == dy[i]:
                        percentage = 0.1
                    else:
                        percentage = 0.01
                    scatter(nnx,nny,dust*percentage)
                    dust_after -= math.floor(dust*percentage)
            else:
                for l in [1,-1]:
                    nnx = nx + l
                    nny = ny + dy[j]
                    if l == dx[i]:
                        percentage = 0.1
                    else:
                        percentage = 0.01
                    scatter(nnx,nny,dust*percentage)
                    dust_after -= math.floor(dust*percentage)
    scatter(nx+dx[i],ny+dy[i],dust_after)

N = int(input())
field = [list(map(int,input().split())) for _ in range(N)]
time, dir_time, dir_num = 1,1,0
start_x, start_y = N//2, N//2
ans = 0
while time < N**2:
    for _ in range(2):
        for _ in range(math.floor(dir_time)):
            time += 1
            tornado(start_x,start_y,dir_num)
            start_x += dx[dir_num]
            start_y += dy[dir_num]
            if start_x == 0 and start_y == 0:
                print(ans)
                exit()
        if dir_num == 3:
            dir_num = 0
        else:
            dir_num += 1
        dir_time += 0.5
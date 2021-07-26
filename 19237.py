from collections import deque

def turnabout(shark_num,dir_num):
    comp = prior[shark_num-1][dir_num]
    if  comp == 1:
        return -1, 0, comp
    elif comp == 2:
        return 1, 0, comp
    elif comp == 3:
        return 0, -1, comp
    else:
        return 0, 1, comp

def fade():
    for i in visited:
        for j in i:
            if j[1] != 0:
                j[1] -= 1
                if j[1] == 0:
                    j[0] = 0
            if j[0] < 0:
                j[0] *= -1

def bfs(queue,left_shark):
    count,answer = 0,0
    while left_shark > 1:
        x,y = queue.popleft()
        shark_num = visited[x][y][0]
        tmp, flag = [], False
        for i in range(4):
            dx, dy, changed_direction = turnabout(shark_num,(direction[shark_num-1]-1)*4+i)
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny][0] == shark_num:
                    tmp.append([nx,ny,changed_direction])
                elif visited[nx][ny][0] == 0:
                    flag = True
                    location.append([nx,ny])
                    visited[nx][ny] = [shark_num,K+1]
                    direction[shark_num-1] = changed_direction
                    break
                else:
                    if visited[nx][ny][0] > 0 and visited[nx][ny][1] == K+1:
                        flag = True
                        left_shark -= 1
                        count -= 1
                        break
        if not flag:
            location.append(tmp[0][:2])
            visited[tmp[0][0]][tmp[0][1]] = [-shark_num,K+1]
            direction[shark_num-1] = tmp[0][2]
        count += 1
        if count == left_shark:
            fade()
            count = 0
            answer += 1 
        if answer > 1000:
            return -1
    return answer
                
N, M, K = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(N)]
location = [[0,0] for _ in range(M)]
visited = [[[0,0] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if field[i][j] != 0:
            location[field[i][j]-1] = [i,j]
            visited[i][j] = [field[i][j],K]
location = deque(location)
direction = list(map(int,input().split()))
prior = [list(map(int,input().split())) + list(map(int,input().split())) + list(map(int,input().split())) + list(map(int,input().split())) for _ in range(M)]
print(bfs(location,len(location)))
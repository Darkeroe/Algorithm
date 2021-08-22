dx = [0,0,-1,1]
dy = [1,-1,0,0]

def move(piece,num):
    x, y, z, arr, cnt = piece[0]-1, piece[1]-1, piece[2]-1, [], 0
    max_height = len(location[x][y])
    for i in range(3):
        if location[x][y][i] == num:
            height = i
            break
    for i in range(height,max_height):
        nx = x+dx[z]
        ny = y+dy[z]
        if not 0 <= nx < n or not 0 <= ny < n or board[nx][ny] == 2:
            nx = x-dx[z]
            ny = y-dy[z]
            if cnt == 0:
                if inven[num-1][2] == 1: inven[num-1][2] = 2
                elif inven[num-1][2] == 2: inven[num-1][2] = 1
                elif inven[num-1][2] == 3: inven[num-1][2] = 4
                else: inven[num-1][2] = 3
            cnt += 1
            if not 0 <= nx < n or not 0 <= ny < n or board[nx][ny] == 2:
                return 0;
            else:
                tmp = location[x][y].pop(height)
                arr.append(tmp)
                inven[tmp-1][0] -= dx[z]
                inven[tmp-1][1] -= dy[z]
        else:
            tmp = location[x][y].pop(height)
            arr.append(tmp)
            inven[tmp-1][0] += dx[z]
            inven[tmp-1][1] += dy[z]
    if board[nx][ny] == 1:
        arr.reverse()
    for i in arr:
        location[nx][ny].append(i)
        if len(location[nx][ny]) >= 4:
            return True
    return False

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
inven = [list(map(int,input().split())) for _ in range(m)]
location = [[[] for _ in range(n)] for _ in range(n)]
cnt = 1
for i in inven:
    location[i[0]-1][i[1]-1].append(cnt)
    cnt += 1
sol,end = 1,0
while True:
    cnt = 1
    for i in inven:
        if move(i,cnt) == True:
            end += 1
            print(sol)
            break
        cnt += 1
    if end == 1:
        break
    elif sol > 1000:
        print(-1)
        break
    sol += 1

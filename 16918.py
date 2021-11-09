import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [-1,1,0,0]

R,C,N = map(int,input().split())
board = [list(map(str,str(input().rstrip()))) for _ in range(R)]

if N%2 == 0:
    print(*(['O'*C]*R), sep='\n')

else:
    bomb1,bomb2,flag,cnt = {},{},True,True
    visited = [[True for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bomb1[(i,j)] = 1
                visited[i][j] = False
            else:
                bomb2[(i,j)] = 1
                
    for _ in range(N//2):
        if flag:
            target,storage = bomb1,bomb2
            flag = False
        else:
            target,storage = bomb2,bomb1
            flag = True
        tmp = []
        for i in target:
            for j in range(4):
                nx = i[0]+dx[j]
                ny = i[1]+dy[j]
                if 0<=nx<R and 0<=ny<C and visited[nx][ny] == cnt:
                    visited[nx][ny] = not cnt
                    tmp.append((nx,ny))
                    del storage[(nx,ny)]
        for i in tmp:
            target[i] = 1
        cnt = not cnt

    if flag:
        ans = bomb1
    else:
        ans = bomb2

    for i in range(R):
        for j in range(C):
            if (i,j) in ans:
                board[i][j] = 'O'
            else:
                board[i][j] = '.'
    for i in board:
        print("".join(i))
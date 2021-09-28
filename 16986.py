from itertools import permutations
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
match = [list(map(int,input().split())) for _ in range(N)]
player = [list(permutations([i for i in range(1,N+1)],N))]
print(player)

for _ in range(2):
    player.append(list(map(int,input().split())))

for i in range(len(player[0])):
    idx0,idx1,idx2 = 0,0,0
    win = [0,0,0]
    a,b,left = 0,1,2
    while True:
        if a == 0:
            x = player[a][i][idx0]-1
            idx0 += 1
            if b == 1:
                y = player[b][idx1]-1
                idx1+=1
            else:
                y = player[b][idx2]-1
                idx2+=1
        elif b == 0:
            y = player[b][i][idx0]-1
            idx0 += 1
            if a == 1:
                x = player[a][idx1]-1
                idx1+=1
            else:
                x = player[a][idx2]-1
                idx2+=1
        else:
            if a == 1:
                x = player[a][idx1]-1
                y = player[b][idx2]-1
            else:
                x = player[a][idx2]-1
                y = player[b][idx1]-1
            idx1 += 1
            idx2 += 1

        if match[x][y] == 0 or (match[x][y] == 1 and a<b):
            win[b] += 1
            a, left = left, a
        elif match[x][y] == 2 or (match[x][y] == 1 and a>b):
            win[a] += 1
            b, left = left, b

        if max(win) == K:
            if win.index(K) == 0:
                print(1)
                exit()
            else:
                break
        if idx0 == N:
            break
print(0)
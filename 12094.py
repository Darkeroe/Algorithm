from sys import stdin
from math import log2
from math import floor
from collections import deque

def move(c_cube,idx,cnt,limit):
    flag, layer_x = False, 0
    c_cube_ud = [[] for _ in range(N)]
    c_cube_lr = [[] for _ in range(N)]
    for i in c_cube:
        if idx == 0:
            a, b, c, layer_y, const = 1, len(i), 1, 0, -1
        else:
            a, b, c, layer_y, const =  len(i)-2 , -1, -1, N-1, 1
        if len(i) == 1:
            c_cube_ud[layer_x].append(i[0])
            c_cube_lr[layer_y].append(i[0])
            layer_x += 1
            continue

        skip = False
        for j in range(a,b,c):
            tmp = i[j]
            if not skip:
                if i[j] == i[j+const]:
                    flag = True
                    c_cube_ud[layer_x].append(tmp*2)
                    c_cube_lr[layer_y].append(tmp*2)
                    if idx == 0:
                        layer_y += 1
                    else:
                        layer_y -= 1
                    if tmp*2 > limit:
                        limit = tmp*2
                    skip = True
                else:
                    if idx == 0:
                        c_cube_ud[layer_x].append(i[j-1])
                        c_cube_lr[layer_y].append(i[j-1])
                        layer_y += 1
                    else:
                        c_cube_ud[layer_x].append(i[j+1])
                        c_cube_lr[layer_y].append(i[j+1])
                        layer_y -= 1
                    if (idx == 0 and j == len(i)-1) or (idx == 1 and j==0):
                        c_cube_ud[layer_x].append(tmp)
                        c_cube_lr[layer_y].append(tmp)
                        break
            else:
                if (idx == 0 and j == len(i)-1) or (idx == 1 and j== 0):
                    c_cube_ud[layer_x].append(tmp)
                    c_cube_lr[layer_y].append(tmp)
                    if idx == 0:
                        layer_y += 1
                    else:
                        layer_y -= 1
                else:
                    skip = False
        if idx == 1:
            c_cube_ud[layer_x].reverse()
        layer_x += 1

    if limit >= summation:
        print(limit)
        exit()

    if arr[9] < limit:
        tmp = 1
        for i in range(9,-1,-1):
            arr[i] = limit//tmp
            tmp *= 2
    if (cnt == 0) or (cnt+1 <= 9 and limit > arr[cnt]):
        if flag == False:
            prog(cnt+1,c_cube_ud,c_cube_lr,limit,0)
        else:
            prog(cnt+1,c_cube_ud,c_cube_lr,limit,1)

def prog(cnt,cube1,cube2,limit,skip):
    if skip == 1:
        for i in range(2):
            move(cube1,i,cnt,limit)
            move(cube2,i,cnt,limit)
    else:
        for i in range(2):
            move(cube2,i,cnt,limit)

N = int(stdin.readline())
cube_ud, cube_lr, summation = [[] for _ in range(N)], [[] for _ in range(N)], 0
empty = [[] for _ in range(N)]
for i in range(N):
    tmp = [*map(int, stdin.readline().split())]
    for j in range(N):
        if tmp[j] != 0:
            cube_ud[i].append(tmp[j])
            cube_lr[j].append(tmp[j])
            summation += tmp[j]
if N == 1:
    print(cube_ud[0][0])
    exit()

# largest power of 2 less than the sum of all blocks
summation = 2**(floor(log2(summation)))

ans = 0
for i in cube_ud:
    if i != [] and max(i) > ans:
        ans = max(i)

arr, tmp, length = [0 for _ in range(10)], 1, len(cube_ud)
# minimim number to have in each move
for i in range(9,-1,-1): 
    arr[i] = ans//tmp
    tmp *= 2

prog(0,cube_ud,cube_lr,ans,1)
print(arr[9])
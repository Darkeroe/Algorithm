from copy import deepcopy
from itertools import combinations
import sys
input = sys.stdin.readline

N,M,D = map(int,input().split())
board_original = [list(map(int,input().split())) for _ in range(N)]
cand = combinations([i for i in range(M)],3)
ans = 0
for archer_list in cand:
    board = deepcopy(board_original)
    tmp = 0
    for j in range(N,0,-1):
        for archer in archer_list:
            flag = True
            for k in range(1,D+1):
                for l in range(-k+1,k):
                    if abs(k-abs(l))+abs(l) <= D:
                        x,y = j-k+abs(l),archer+l
                        if 0<=x and 0<=y<M:
                            if board[x][y] == 1:
                                board[x][y] = -1*j
                                tmp += 1
                                flag = False
                                break
                            elif board[x][y] == -1*j:
                                flag = False
                                break
                if not flag:
                    break
    ans = max(ans,tmp)
print(ans)
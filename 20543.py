import sys
input = sys.stdin.readline

N,M = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(N)]
ans = [[0 for _ in range(N)] for _ in range(N)]

r = M//2
for i in range(r,N-r):
    for j in range(r,N-r):
        ans[i][j] = -ground[i-r][j-r]
        if j-r-1 >= 0:
            ans[i][j] += ground[i-r][j-r-1]
        if i-r-1 >= 0:
            ans[i][j] += ground[i-r-1][j-r] 
            if j-r-1 >= 0 :
                ans[i][j] -= ground[i-r-1][j-r-1]
        if i >= M:
            ans[i][j] += ans[i-M][j] 
        if j >= M:
            ans[i][j]+= ans[i][j-M]
        if i >= M and j >= M:
            ans[i][j] -= ans[i-M][j-M]
    
for i in ans:
    print(*i)
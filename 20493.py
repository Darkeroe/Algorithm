import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,-1,0,1]
N, T = map(int,input().split())
order = [list(map(str,input().split())) for _ in range(N)]
direction = [0,0]
tmp, pre = 0, 0
for i in order:
    cnt = int(i[0]) - pre
    pre = int(i[0])
    direction[0] += dx[tmp]*cnt
    direction[1] += dy[tmp]*cnt
    if i[1][0] == 'r':
        tmp += 1
    else:
        tmp += 3
    tmp %= 4
direction[0] += dx[tmp]*(T-pre)
direction[1] += dy[tmp]*(T-pre)
print(direction[0], direction[1])

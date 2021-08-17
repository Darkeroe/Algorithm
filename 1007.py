from math import sqrt
from itertools import combinations

T = int(input())
for _ in range(T):
    N = int(input())
    sum_x, sum_y = 0, 0
    coordinate = [list(map(int,input().split())) for _ in range(N)]
    for i in coordinate:
        sum_x += i[0]
        sum_y += i[1]
    comb = combinations(coordinate,N//2)
    ans = float('inf')
    for i in comb:
        tmp_x, tmp_y = sum_x, sum_y
        for j in i:
            tmp_x -= 2*j[0]
            tmp_y -= 2*j[1]
        if ans > sqrt(tmp_x**2 + tmp_y**2):
            ans = sqrt(tmp_x**2 + tmp_y**2)
    print(ans)
import sys
input = sys.stdin.readline

N = int(input())
police = [list(map(int,input().split())) for _ in range(N)]
thieve = list(map(int,input().split()))

ans = [1,1,1,1]
for i in range(4):
    for j in police:
        if i == 0 and thieve[0] > j[0] and abs(thieve[1]-j[1]) <= abs(thieve[0]-j[0]):
            ans[i] = False
        elif i == 1 and thieve[0] < j[0] and abs(thieve[1]-j[1]) <= abs(thieve[0]-j[0]):
            ans[i] = False
        elif i == 2 and thieve[1] > j[1] and abs(thieve[0]-j[0]) <= abs(thieve[1]-j[1]):
            ans[i] = False
        elif i == 3 and thieve[1] < j[1] and abs(thieve[0]-j[0]) <= abs(thieve[1]-j[1]):
            ans[i] = False
            
if True in ans:
    print('YES')
else:
    print('NO')
N,C = map(int,input().split())
M = int(input())
box = [list(map(int,input().split())) for _ in range(M)]
box.sort(key = lambda x : (x[1]))
truck = [C for _ in range(N-1)]
ans = 0

for i in box:
    tmp = min(truck[i[0]-1:i[1]-1])
    if tmp >= i[2]:
        ans += i[2]
        for j in range(i[0]-1,i[1]-1):
            truck[j] -= i[2]
    elif tmp != 0:
        ans += tmp
        for j in range(i[0]-1,i[1]-1):
            truck[j] -= tmp
print(ans)


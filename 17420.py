import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
arr = [0 for _ in range(N)]
for i in range(N):
    arr[i] = [B[i],A[i]]
arr.sort(key = lambda x: (x[0], -x[1]))
ans,comp,limit,tmp2 = 0,0,0,0
for i in range(N):
    b,a = arr[i]
    if max(comp,b) > a:
        tmp = (max(comp,b)-a)//30+1
        if a+(tmp-1)*30 == max(comp,b):
            tmp -= 1
        if tmp > 0:
            ans += tmp
        limit = a + tmp*30
    else:
        limit = max(limit,a)
    if i != N-1:
        if arr[i+1][0] != b:
            comp = max(limit,tmp2)
            tmp2 = 0
        else:
            tmp2 = max(limit,tmp2)
print(ans)
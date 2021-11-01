from collections import deque
import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
arr = {}
for _ in range(N-1):
    a,b,U = map(int,input().split())
    for i in range(2):
        if i == 1:
            a,b = b,a
        if a in arr:
            tmp = arr[a]
            tmp.append((b,U))
            arr[a] = tmp
        else:
            arr[a] = [(b,U)]

for _ in range(Q):
    ans = 0
    k,v = map(int,input().split())
    queue = deque()
    queue.append((0,v,float('inf')))
    while queue:
        prior,V,tmp = queue.pop()
        for i in arr[V]:
            if i[0] != prior:
                if min(tmp,i[1]) >= k:
                    ans += 1
                queue.append((V,i[0],min(tmp,i[1])))
    print(ans)
import sys
input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v,u):
    a = find(v)
    b = find(u)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a

N,M = map(int,input().split())
sex = list(map(str,input().split()))
dis = [list(map(int,input().split())) for _ in range(M)]

dis = sorted(dis, key = lambda x : x[2])
parent, ans, cnt = list(range(N+1)), 0, 0
for i in dis:
    a,b,cost = i
    if sex[a-1] == sex[b-1]:
        continue
    elif find(a) != find(b):
        union(a,b)
        ans += cost
        cnt += 1

if cnt < N-1:
    print(-1)
else:
    print(ans)
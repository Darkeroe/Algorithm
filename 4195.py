import sys
input = sys.stdin.readline

def find(v):
    if v == parent[v]:
        return v
    else:
        tmp = find(parent[v])
        parent[v] = tmp
        return parent[v]

def union(v,u):
    a = find(v)
    b = find(u)

    if a != b:
        parent[b] = a
        num[a] += num[b]

N = int(input())
for _ in range(N):
    F = int(input())
    parent, num = {}, {}

    for _ in range(F):
        a,b = map(str,input().rstrip().split(" "))
        if a not in parent:
            parent[a] = a
            num[a] = 1
        if b not in parent:
            parent[b] = b
            num[b] = 1
        union(a,b)
        print(num[find(a)])
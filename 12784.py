import sys
input = sys.stdin.readline

def divide(parent,node):
    for i in range(len(arr[node])):
        if arr[node][i][0] != parent:
            leaf(node,arr[node][i][0])
    return 0

def leaf(parent,node):
    global answer
    if len(arr[node]) == 1:
        leaf_arr.append(node)
        dp[node] = arr[node][0][1]
    else:
        for i in arr[node]:
            if i[0] != parent:
                leaf(node,i[0])
            else:
                dp[node] = i[1]
    return 0

def search(parent, child):
    tmp = 0
    for i in arr[child]:
        if i[0] != parent:
            if i[0] not in leaf_arr:
                tmp += search(child,i[0])
            else:
                tmp += dp[i[0]]
    dp[child] = min(dp[child],tmp)
    return dp[child]

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    dp = [float('inf') for _ in range(N)]
    arr = [[] for _ in range(N)]
    leaf_arr = []
    for _ in range(M):
        a,b,c = map(int,input().split())
        arr[a-1].append([b-1,c])
        arr[b-1].append([a-1,c])
    divide(0,0)
    search(0,0)
    print(dp[0])
T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    D = list(map(int,input().split()))
    stack = []
    arr = [0 for _ in range(N)]
    order = [[] for _ in range(N)]
    dp = [[] for _ in range(N)]
    ans = 0
    
    for _ in range(K):
        a,b = map(int,input().split())
        arr[b-1] += 1
        order[a-1].append(b-1)
    win = int(input())

    for i in range(N):
        if arr[i] == 0:
            stack.append(i)
            dp[i].append(0)

    while stack:
        c = stack.pop()
        dp[c] = [max(dp[c]) + D[c]]
        if c == win-1:
            print(dp[c][0])
            break
        for i in order[c]:
            arr[i] -= 1
            dp[i].append(dp[c][0])
            if arr[i] == 0:
                stack.append(i)
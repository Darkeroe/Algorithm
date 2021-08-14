def floyd_warshall(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if j == k:
                    arr[j][k] = 0
                else:
                    arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])
    return arr

n = int(input())
m = int(input())
arr = [list(map(int,input().split())) for i in range(m)]
cost = [[float('inf') for i in range(n)] for j in range(n)]
for i in arr:
    if cost[i[0]-1][i[1]-1] > i[2]:
        cost[i[0]-1][i[1]-1] = i[2]
for i in floyd_warshall(cost):
    for j in range(n):
        if i[j] == float('inf'):
            i[j] = 0
        print(i[j], end=' ')
    print(sep='\n')


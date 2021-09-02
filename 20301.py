import sys
input = sys.stdin.readline

N, K, M = map(int,input().split())
arr, idx, reverse, tmp = list(range(1,N+1)), K-1, 0, 1
while arr:
    print(arr.pop(idx))
    reverse += 1
    if reverse == M:
        reverse = 0
        tmp *= -1
    idx += (tmp*K)-(tmp+1)//2
    if arr and (idx >= len(arr) or idx < 0):
        idx = idx%len(arr)
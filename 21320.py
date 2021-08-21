import sys
input = sys.stdin.readline
mod = 1000000007
N, K = map(int,input().split())
arr = [0 for _ in range(N)]
for i in range(2,N):
    if i % 2 == 0:
        arr[i] = arr[i-1]*2+2
    else:
        arr[i] = arr[i-1]*2
if (N + K) % 2 == 0:
    print(arr[N-1]%mod)
else:
    print(arr[N-1]%mod+1)
N = int(input())
K = int(input())
arr = list(map(int,input().split()))
arr.sort()
diff = []
for i in range(N-1):
    diff.append(arr[i+1]-arr[i])
diff.sort(reverse=True)
ans = arr[N-1] - arr[0]
if K-1 > len(diff):
    tmp = len(diff)
else:
    tmp = K-1
for i in range(tmp):
    ans -= diff[i]
print(ans)
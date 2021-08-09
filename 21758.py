N = int(input())
field = list(map(int,input().split()))

arr1 = [0 for _ in range(N)]
arr2 = [0 for _ in range(N)]
ans = 0
def summation(arr,flag):
    global ans
    for j in range(1,N-1):
        if flag == 0:
            tmp = arr[N-1] - field[0] - field[j]
        else:
            tmp = arr[N-1] - field[N-1] - field[N-1-j]
        tmp += arr[N-1] - arr[j]
        if tmp > ans:
            ans = tmp

arr1[0] = field[0]
arr2[0] = field[N-1]
for i in range(1,N):
    arr1[i] = arr1[i-1] + field[i]
    arr2[i] = arr2[i-1] + field[N-1-i]
summation(arr1,0)
summation(arr2,1)

arr1[N-1] = field[N-1]

for j in range(N-2,0,-1):
    tmp = 2*field[j]
    tmp += arr1[j-1] - field[0]
    tmp += arr1[j+1] - field[N-1]
    if tmp > ans:
        ans = tmp
    arr1[j] = arr1[j+1] + field[j]
print(ans)
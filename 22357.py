K, N = map(int,input().split())
arr, tmp= [], N

while len(arr) < K:
    for i in range(tmp,2500):
        result = True
        for j in range(2,int(i**(1/2))+1):
            if (i%j == 0):
                result = False
        if result:
            arr.append(i)
            tmp += 1
            break
        tmp += 1

for i in range(K):
    for j in range(N):
        if j == N-1:
            print(arr[i]*(j+1))
        else:
            print(arr[i]*(j+1),end=' ')
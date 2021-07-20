N, M, T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
point, total = N*M, 0
for i in arr:
    total += sum(i)

for _ in range(T):
    x,d,k = map(int,input().split())
    k %= M
    tmp_x, flag, cnt = x, True, 1

    if point != 0:
        sol = total/point
    else:
        total = 0
        break

    while len(arr) >= tmp_x:
        if d == 0:
            tmp_arr = arr[tmp_x-1][M-k:]
            arr[tmp_x-1] = tmp_arr + arr[tmp_x-1][:M-k]
        else:
            tmp_arr = arr[tmp_x-1][k:]
            arr[tmp_x-1] = tmp_arr + arr[tmp_x-1][:k] 
        tmp_x += x

    for i in arr:
        for j in range(M):
            if j == M-1:
                if i[j] != 0 and abs(i[j]) == abs(i[0]):
                    i[j], i[0] = -abs(i[j]), -abs(i[0])
                    flag = False
            else:
                if i[j] != 0 and abs(i[j]) == abs(i[j+1]):
                    i[j], i[j+1] = -abs(i[j]), -abs(i[j+1])
                    flag = False
            if i[j] != 0 and cnt != N and abs(i[j]) == arr[cnt][j]:
                i[j], arr[cnt][j] = -abs(i[j]), -arr[cnt][j]
                flag = False
        cnt += 1
        
    if flag == True:
        for i in arr:
            for j in range(M):
                if i[j] != 0 and i[j] > sol:
                    i[j] -= 1
                    total -= 1
                elif 0 < i[j] < sol:
                    i[j] += 1  
                    total += 1  
    else:
        for i in arr:
            for j in range(M):
                if i[j] < 0:
                    total += i[j]
                    point -= 1
                    i[j] = 0
print(total)
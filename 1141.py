N = int(input())
arr = []
for i in range(N):
    arr.append(str(input()))
arr.sort(key=len)
ans, cnt = 0, 1
for i in arr:
    flag = True
    for j in arr[cnt:]:
        if i == j[:len(i)]:
            flag = False
            break
    if flag:
        ans += 1
    cnt += 1
print(ans)
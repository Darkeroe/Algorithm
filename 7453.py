n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]


ret = [[0]*len(arr) for _ in range(4)]
for i in range(4):
    for j in range(n):
        if i == 2 or i == 3:
            ret[i][j] = [arr[j][i],i]
        else: 
            ret[i][j] = arr[j][i]
# ret[0].sort()
# ret[1].sort()
ret[2] = ret[2] + ret[3]
ret[2].sort()
# ret[3].sort()
# for i in range(3):
#     print(ret[i])
# start, end = 0, len(ret[2])-1
count = 0
pls = []
for i in range(n):
    for j in range(n):
        pls.append(ret[0][i] + ret[1][j])

for i in pls:
    start, end = 0, len(ret[2])-1
    tar = i
    while start < end:
        # print('a+b=-c',ret[2][start][0],ret[2][end][0],tar)
        if ret[2][start][0] +ret[2][end][0] == -(tar) and ret[2][start][1] != ret[2][end][1]:
            count += 1
        if ret[2][start][0] + ret[2][end][0] > -(tar):
            end -= 1
        else:
            start +=1
    
print(count)

# for i in ret[1]:
#     print(i[0])
#     # print(i)


# -1 -2 -3 4 5 6 7 8  98
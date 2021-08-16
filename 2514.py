M = int(input())
K = int(input())
field = [list(map(int,input().split())) for _ in range(8)]
original = M*15
tmp = [[M for _ in range(8)] for _ in range(8)]
ans = [[] for _ in range(8)]
arr = []
def demo(x,y):
    for i in range(8):
        tmp[x][i] += 1
        tmp[i][y] += 1
    tmp[x][y] -= 1

def compare(x,y):
    tmp = sum(field[x]) - field[x][y]
    for i in range(8):
        tmp += field[i][y]
    if (original - tmp) % 2 == 1:
        return True
    else:
        return False

def compare2(x,y):
    sum1 = sum(field[x]) - field[x][y]
    sum2 = sum(tmp[x]) - tmp[x][y]
    for i in range(8):
        sum1 += field[i][y]
        sum2 += tmp[i][y]
    if (sum2 - sum1) % 4 == 2:
        return False
    return True

for i in range(8):
    for j in range(8):
        if compare(i,j):
            demo(i,j)
            arr.append([i,j])
            ans[i].append('+')
        else:
            ans[i].append('.')

for i in arr:
    if not compare2(i[0],i[1]):
        ans[i[0]][i[1]] = '-'

for i in ans:
    for j in i:
        print(j,end = ' ')
    print()
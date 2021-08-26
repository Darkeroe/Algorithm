import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int,input().split()))
idx = -1
print(0, end = ' ')
for i in range(N):
    for j in range(i-1,idx,-1):
        if tower[idx+1] < tower[j]:
            idx = j-1
        if tower[i] < tower[j]:
            print(j+1,end=' ')
            break
        elif j == idx + 1:
            print(0,end=' ')

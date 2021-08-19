import sys
N, K, P, X = map(int,sys.stdin.readline().split())
a0 = [0, 4, 3, 3, 4, 3, 2, 3, 1, 2]
a1 = [4, 0, 5, 3, 2, 5, 6, 1, 5, 4]
a2 = [3, 5, 0, 2, 5, 4, 3, 4, 2, 3]
a3 = [3, 3, 2, 0, 3, 2, 3, 2, 2, 1]
a4 = [4, 2, 5, 3, 0, 3, 4, 3, 3, 2]
a5 = [3, 5, 4, 2, 3, 0, 1, 4, 2, 1]
a6 = [2, 6, 3, 3, 4, 1, 0, 5, 1, 2]
a7 = [3, 1, 4, 2, 3, 4, 5, 0, 4, 3]
a8 = [1, 5, 2, 2, 3, 2, 1, 4, 0, 1]
a9 = [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
a = [a0]+[a1]+[a2]+[a3]+[a4]+[a5]+[a6]+[a7]+[a8]+[a9]
res = 0

def to_arr(num,arr):
    while num!=0:
        arr.append(num % 10)
        num = num//10
    while len(arr) != K:
        arr.append(0)

display = []
to_arr(X,display)
for i in range(1,N+1):
    tmp = []
    to_arr(i,tmp)
    ans = P
    for j in range(K):
        ans -= a[display[j]][tmp[j]]
    if ans >= 0:
        res += 1
print(res-1)
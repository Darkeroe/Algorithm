import sys
input = sys.stdin.readline

def to_bit(arr):
    bit = []
    for i in arr:
        tmp = 0
        for j in range(1,i[0]+1):
            tmp += 2**(i[j]-1)
        bit.append(tmp)
    return bit

N = int(input())
subject = [list(map(int,input().split())) for _ in range(N)]
A = to_bit(subject)

M = int(input())
student = [list(map(int,input().split())) for _ in range(M)]
B = to_bit(student)

for i in B:
    cnt = 0
    for j in A:
        if j == (i & j):
            cnt += 1
    print(cnt)
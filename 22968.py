import sys
input = sys.stdin.readline

T = int(input())
V = [int(input()) for _ in range(T)]

def tree():
    arr = [i for i in range(45)]
    for i in range(2,45):
        arr[i] = arr[i-1]+arr[i-2]
    for i in range(1,45):
        arr[i] += arr[i-1]
    return arr

arr = tree()
for i in V:
    cnt = -1
    for j in arr:
        if i < j:
            print(cnt)
            break
        cnt += 1
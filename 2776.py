# dictionary 사용
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr1 = list(map(int,input().split()))
    dic = {int: 0 for int in arr1}
    M = int(input())
    arr2 = list(map(int,input().split()))
    for i in arr2:
        if i in dic:
            print(1)
        else:
            print(0)

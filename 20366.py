from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
snowball = list(map(int,input().split()))
tmp = [i for i in range(N)]
comb = list(combinations(tmp,2))
arr,answer = [],float('inf')

for i in comb:
    arr.append([snowball[i[0]]+snowball[i[1]],i])
arr = sorted(arr, key=lambda x: x[0])

for i in range(len(arr)-1):
    if abs(arr[i][0] - arr[i+1][0]) < answer and arr[i][1][0] not in arr[i+1][1] and arr[i][1][1] not in arr[i+1][1]:
            answer = abs(arr[i][0] - arr[i+1][0])

print(answer)
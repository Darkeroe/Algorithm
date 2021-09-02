import sys
input = sys.stdin.readline

n = int(input())
arr, tmp, primes_odd, primes_even, flag = [False,False] + [True]*100000, 0, [[0,0],[0,0]], [[0,0],[0,0]], True
for i in range(n):
    a,b = map(int,input().split())
    if i == 0:
        start, tmp = 2, b
    elif tmp < b:
        start, tmp = tmp+1, b
    else:
        start = b+1
    for j in range(start,b+1):
        if arr[j]:
            if flag:
                primes_odd.append([primes_odd[-1][0] + 3*j,0])
                if j != 2:
                    primes_even.append([primes_even[-1][0] - j,1])
                else:
                    primes_even.append([0,0])
                flag = False
            else:
                primes_odd.append([primes_odd[-1][0] - j,1])
                primes_even.append([primes_even[-1][0] + 3*j,0])
                flag = True
            for k in range(2*j,100000,j):
                arr[k] = False
        else:
            primes_even.append([primes_even[-1][0],primes_even[-1][1]])
            primes_odd.append([primes_odd[-1][0],primes_odd[-1][1]])
    
    if primes_odd[a][1] == primes_odd[a-1][1] and a != 1 and a != 2:
        if primes_odd[a][1] == 1:
            print(primes_odd[b][0] - primes_odd[a-1][0])
        else:
            print(primes_even[b][0] - primes_even[a-1][0])
    else:
        if primes_odd[a][1] == 0:
            print(primes_odd[b][0] - primes_odd[a-1][0])
        else:
            print(primes_even[b][0] - primes_even[a-1][0])

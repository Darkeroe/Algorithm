import sys
input = sys.stdin.readline
T = int(input())

def summation(N):
    b,tmp = 1,N
    N -= 1
    arr = []
    while N > 0:
        b += 1
        N = N-b
        cand = []

        if (N%b == 0):
            for i in range(1, b+1):
                num = int((N/b)+i)
                cand.append(num)
                arr.append(cand)
    if arr:
        ans = (min(arr, key=len))
        return str(tmp) + " = " +' + '.join(str(x) for x in ans)
    else:
        return "IMPOSSIBLE"

for _ in range(T):
    N = int(input())
    print(summation(N))
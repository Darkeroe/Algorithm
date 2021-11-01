import sys
input = sys.stdin.readline

M,N = map(int,input().split())
honeycomb = [1 for _ in range(M)]
honeycomb2 = [1 for _ in range(M-1)]
for _ in range(N):
    a,b,c = map(int,input().split())
    for i in range(M-1,-1,-1):
        if a != 0:
            a -= 1
        else:   
            if b != 0:
                honeycomb[i] += 1
                b -= 1
            else:
                if c != 0:
                    honeycomb[i] += 2
                    c -= 1
    for i in range(M):
        if a != 0:
            a -= 1
        else:   
            if b != 0:
                honeycomb2[i] += 1
                b -= 1
            else:
                if c != 0:
                    honeycomb2[i] += 2
                    c -= 1

for i in honeycomb:
    print(i,end = ' ')
    print(*honeycomb2)
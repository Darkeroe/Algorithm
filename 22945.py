import sys
input = sys.stdin.readline

ans = 0
N = int(input())
status = list(map(int,input().split()))
start,end = 0,N-1
while start < end:
    ans = max(ans,(end-start-1)*min(status[start],status[end]))
    if status[end] >= status[start]:
        start += 1
    else:
        end -= 1
print(ans)
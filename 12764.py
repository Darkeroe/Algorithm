from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
usage_time = []
for _ in range(N):
    heappush(usage_time,list(map(int,input().split())))
seats = [0 for _ in range(N)]
cnt = [0 for _ in range(N)]

while usage_time:
    start,end = heappop(usage_time)
    for i in range(len(seats)):
        if seats[i] <= start:
            seats[i] = end
            cnt[i] += 1
            break

for i in range(N):
    if cnt[i] == 0:
        cnt = cnt[:i]
        break

print(len(cnt))
print(*cnt)
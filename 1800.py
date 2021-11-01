from heapq import heappop,heappush
import sys
input = sys.stdin.readline

N,P,K = map(int,input().split())
cable = [[] for _ in range(N+1)]
cand = set()
cand.add(0)
for _ in range(P):
    a,b,c = map(int,input().split())
    cable[a].append((b,c))
    cable[b].append((a,c))
    cand.add(c)
cand = list(cand)
cand.sort()
start, end = 0, len(cand)-1
flag, tmp = True, float('inf')
while flag:
    target = (start+end)//2
    queue = []
    heappush(queue,(0,1))
    ans = [float('inf') for _ in range(N+1)]
    ans[1] = 0
    while queue:
        dist,now = heappop(queue)
        for i in cable[now]:
            copy_dist = dist
            if i[1] > cand[target]:
                copy_dist += 1
            if ans[i[0]] <= copy_dist:
                continue
            if copy_dist <= K:
                ans[i[0]] = copy_dist
                if i[0] == N:
                    flag = False
                    break
                heappush(queue,(copy_dist,i[0]))

    if flag:
        start = target + 1
    else:
        end = target - 1
        tmp = cand[target]
        flag = True
    if start > end:
        if tmp == float('inf'):
            tmp = -1
        break

print(tmp)
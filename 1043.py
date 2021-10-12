import sys
input = sys.stdin.readline

def check(ans):
    length = len(visited)
    cand = []
    for i in visited:
        for j in party[i-1]:
            if j in people:
                ans -= 1
                for k in party[i-1]:
                    people.add(k)
                cand.append(i+1)
                break
    for i in cand:
        visited.remove(i-1)
    if length == len(visited):
        print(ans)
        return 0
    else:
        check(ans)

N,M = map(int,input().split())
tmp = list(map(int,input().split()))
people = set()
if tmp[0] != 0:
    for i in range(tmp[0]):
        people.add(tmp[i+1])

visited,party,ans = set(),[],M
for i in range(M):
    visited.add(i+1)
    party.append(list(map(int,input().split()))[1:])
check(ans)
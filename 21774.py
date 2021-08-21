import datetime
import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
time = []
for _ in range(N):
    t,n = map(str,input().split('#'))
    time.append([datetime.datetime.strptime(t,'%Y-%m-%d %H:%M:%S'),n])
time.sort()
length = len(time)
for _ in range(Q):
    ans = 0
    s,e,n = map(str,input().split('#'))
    s = datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S')
    e = datetime.datetime.strptime(e,'%Y-%m-%d %H:%M:%S')
    for i in time:
        if s<=i[0]<=e and n<=i[1]:
            ans += 1
    print(ans)
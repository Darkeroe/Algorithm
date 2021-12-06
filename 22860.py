import sys
input = sys.stdin.readline

def struct(relation):
    linked = {}
    linked['main'] = ['',{},{}]
    for P,F,C in relation:
        if C == '1':
            try:
                linked[F][0] = P
            except:
                linked[F] = [P,{},{}]
            try:
                linked[P][1][F] = True
            except:
                linked[P] = ['',{},{}]
                linked[P][1][F] = True
        else:
            linked[F] = [P]
            try:
                linked[P][2][F] = True
            except:
                linked[P] = ['',{},{}]
                linked[P][2][F] = True
    return linked

def count(target,store,cnt):
    for folder in main[target][1]:
        store, cnt = count(folder,store,cnt)
        
    for file in main[target][2]:
        store.add(file)
        cnt += 1
    return store,cnt

N,M = map(int,input().split())
relation = [list(str(input()).split()) for _ in range(N+M)]
main = struct(relation)
Q = int(input())
for _ in range(Q):
    query = list(input().rstrip().split('/'))
    ans = count(query[-1],set(),0)
    print(len(ans[0]),ans[1])
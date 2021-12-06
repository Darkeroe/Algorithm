import sys
input = sys.stdin.readline

N = int(input())
problem,number = {},{}
for _ in range(N):
    P,L = map(int,input().split())
    number[P] = L
    try:
        problem[L][P] = True
    except:
        problem[L] = {}
        problem[L][P] = True

M = int(input())
queries = [list(str(input()).split()) for _ in range(M)]

for query in queries:
    if query[0] == 'add':
        number[int(query[1])] = int(query[2])
        try:
            problem[int(query[2])][int(query[1])] = True
        except:
            problem[int(query[2])] = {}
            problem[int(query[2])][int(query[1])] = True
    elif query[0] == 'recommend':
        if query[1] == '1':
            print(max(problem[max(problem)]))
        else:
            print(min(problem[min(problem)]))
    else:
        del problem[number[int(query[1])]][int(query[1])]
        if problem[number[int(query[1])]] == {}:
            del problem[number[int(query[1])]]
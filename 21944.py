import sys
input = sys.stdin.readline

N = int(input())
grade,grade_num,problem,number = {},{},{},{}
for _ in range(N):
    P,L,G = map(int,input().split())
    number[P] = L
    grade_num[P] = G
    try:
        problem[L][P] = True
    except:
        problem[L] = {}
        problem[L][P] = True
    try:
        grade[G][L]
    except:
        try:
            grade[G]
        except:
            grade[G] = {}
        grade[G][L] = []
    grade[G][L].append(P)

M = int(input())
queries = [list(str(input()).split()) for _ in range(M)]

for query in queries:
    if query[0] == 'add':
        number[int(query[1])] = int(query[2])
        grade_num[int(query[1])] = int(query[3])
        try:
            problem[int(query[2])][int(query[1])] = True
        except:
            problem[int(query[2])] = {}
            problem[int(query[2])][int(query[1])] = True
        try:
            grade[int(query[3])][int(query[2])]
        except:
            try:
                grade[int(query[3])]
            except:
                grade[int(query[3])] = {}
            grade[int(query[3])][int(query[2])] = []
        grade[int(query[3])][int(query[2])].append(int(query[1]))
    elif query[0] == 'recommend2':
        if query[1] == '1':
            print(max(problem[max(problem)]))
        else:
            print(min(problem[min(problem)]))
    elif query[0] == 'recommend':
        if query[2] == '1':
            print(max(grade[int(query[1])][max(grade[int(query[1])])]))
        else:
            print(min(grade[int(query[1])][min(grade[int(query[1])])]))
    elif query[0] == 'recommend3':
        if query[1] == '1':
            small = float('inf')
            for i in problem:
                if i >= int(query[2]):
                    small = min(small,i)
            if small == float('inf'):
                print(-1)
            else:
                print(min(problem[small]))
        else:
            big = 0
            for i in problem:
                if i < int(query[2]):
                    big = max(big,i)
            if big == 0:
                print(-1)
            else:
                print(max(problem[big]))
            
    else:
        del problem[number[int(query[1])]][int(query[1])]
        if problem[number[int(query[1])]] == {}:
            del problem[number[int(query[1])]]
        grade[grade_num[int(query[1])]][number[int(query[1])]].remove(int(query[1]))
        if grade[grade_num[int(query[1])]][number[int(query[1])]] == []:
            del grade[grade_num[int(query[1])]][number[int(query[1])]]
            if grade[grade_num[int(query[1])]] == {}:
                del grade[grade_num[int(query[1])]]
import sys
input = sys.stdin.readline

for _ in range(3):
    row = [0 for _ in range(7)]
    column = [0 for _ in range(7)]
    arr = [list(map(int,input().split())) for _ in range(6)]

    flag = True
    for k in range(2):
        for i in range(6):
            tmp = 0
            for j in range(6):
                if k == 0:
                    if arr[i][j] == 0 and tmp != 0:
                        row[i] = tmp
                        row[6] += 1
                        break
                    if arr[i][j] == 1:
                        tmp += 1
                        if j == 5:
                            row[i] = tmp
                            row[6] += 1
                else:
                    if arr[j][i] == 0 and tmp != 0:
                        column[i] = tmp
                        column[6] += 1
                        break
                    if arr[j][i] == 1:
                        tmp += 1
                        if j == 5:
                            column[i] = tmp
                            column[6] += 1

    if column[6] > row[6]:
        column,row = row,column
    elif column[6] == row[6]:
        print('no')
        continue
    if max(column[:6]) == 4 and 0 < column.index(4) < 5:
        if column[column.index(4)+1] == 1 and column[column.index(4)-1] == 1 and row[6] == 4:
            print('yes')
        else:
            print('no')
    elif max(column[:6]) == 3 and column.index(3) < 5 and column[6] == 2 and row[6] == 5:
        if column[column.index(3)+1] == 3:
            print('yes')
        else:
            print('no')
    elif max(column[:6]) == 3 and 0 < column.index(3) < 5:
        if ((column[column.index(3)-1] == 2 and column[column.index(3)+1] == 1) or (column[column.index(3)-1] == 1 and column[column.index(3)+1] == 2)) and row[6] == 4:
            print('yes')
        else:
            print('no')
    elif max(column[:6]) == 2 and column.index(2) < 4:
        if column[column.index(2)+1] == 2 and column[column.index(2)+2] == 2 and row[6] == 4:
            print('yes')
        else:
            print('no')
    else:
        print('no')
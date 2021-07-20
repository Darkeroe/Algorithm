from itertools import product
route1 = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
route2 = [10,13,16,19,25,30,35,40]
route3 = [20,22,24,25,30,35,40]
route4 = [30,28,27,26,25,30,35,40]
route5 = [25,30,35,40]
length = [21, 8, 7, 8, 4]

dice = list(map(int,input().split()))
sol = 0
for i in range(1,3):
    for j in range(1,4):
        for k in product([1,2,3,4],repeat=7):
            piece = [[0,0],[0,0],[0,0],[0,0]]
            tmp_sum = 0
            tmp = [1]
            tmp.append(i)
            tmp.append(j)
            tmp += list(k)
            cnt = 0
            for l in tmp:
                if piece[l-1][1] < length[piece[l-1][0]]-1:
                    if dice[cnt] + piece[l-1][1] > length[piece[l-1][0]]-1:
                        piece[l-1][1] = 100
                    else:
                        piece[l-1][1] += dice[cnt]
                        if piece[l-1][0] == 0:
                            tmp_sum += route1[piece[l-1][1]]
                        elif piece[l-1][0] == 1:
                            tmp_sum += route2[piece[l-1][1]]
                        elif piece[l-1][0] == 2:
                            tmp_sum += route3[piece[l-1][1]]
                        elif piece[l-1][0] == 3:
                            tmp_sum += route4[piece[l-1][1]]
                        else:
                            tmp_sum += route5[piece[l-1][1]]

                    if piece[l-1][0] == 0:
                        if piece[l-1][1] == 5:
                            piece[l-1] = [1,0]
                        elif piece[l-1][1] == 10:
                            piece[l-1] = [2,0]
                        elif piece[l-1][1] == 15:
                            piece[l-1] = [3,0]
                        elif piece[l-1][1] == 20:
                            piece[l-1] = [4,3]
                    elif piece[l-1][0] == 1 or piece[l-1][0] == 3:
                        if piece[l-1][1] >= 4:
                            piece[l-1] = [4,piece[l-1][1]-4]
                    elif piece[l-1][0] == 2:
                        if piece[l-1][1] >= 3:
                            piece[l-1] = [4,piece[l-1][1]-3]

                    cnt += 1
                    dup = 0
                    for p in range(4):
                        if piece[l-1] == piece[p] and piece[l-1][1] != 100:
                            dup += 1
                    if dup >= 2:
                        tmp_sum = 0
                        break
            if tmp_sum > sol:
                sol = tmp_sum
print(sol)

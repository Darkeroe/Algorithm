def erase(color):
    point = 0
    for i in range(2,6):
        if 0 not in color[i]:
            del color[i]
            color.insert(0,[0,0,0,0])
            point += 1
    if 1 in color[0]:
        del color[4]
        del color[4]
        color.insert(0,[0,0,0,0])
        color.insert(0,[0,0,0,0])
    elif 1 in color[1]:
        del color[5]
        color.insert(0,[0,0,0,0])
    return point

def domino(t,x,y,color):
    if t == 1 or t == 3:
        for i in range(1,5):
            if color[i+1][y] == 1:
                color[i][y] = 1
                if t == 3: 
                    color[i-1][y] = 1 
                break
            if i == 4:
                color[5][y] = 1
                if t == 3: 
                    color[4][y] = 1
    else:
        for i in range(1,5):
            if color[i+1][y] == 1 or color[i+1][y+1] == 1:
                color[i][y], color[i][y+1] = 1, 1
                break
            if i == 4:
                color[5][y], color[5][y+1] = 1, 1
    return erase(color)

n = int(input())
order = [list(map(int,input().split())) for _ in range(n)]
green, blue = [[0,0,0,0] for _ in range(6)], [[0,0,0,0] for _ in range(6)]
answer,block = 0,0
for i in order:
    answer += domino(i[0],i[1],i[2],green)
    if i[0] == 3:
        i[0] = 2
        if i[1] == 0:
            i[1] = 2
        elif i[1] == 2:
            i[1] = 0
    else:
        if i[0] == 2:
            i[0] =3
        if i[1] == 0:
            i[1] = 3
        elif i[1] == 1:
            i[1] = 2
        elif i[1] == 2:
            i[1] = 1
        else:
            i[1] = 0
    answer += domino(i[0],i[1],i[1],blue)
    
for i in green:
    block += i.count(1)
for i in blue:
    block += i.count(1)
print(answer)
print(block)
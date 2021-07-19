N, H = map(int,input().split())
top, bottom, res = [0] * H, [0] * H, [0] * H

for i in range(N//2):
    bottom[int(input())-1] += 1
    top[int(input())-1] += 1
    print(bottom)
    print(top)
print() 

for i in range(H-2,-1,-1):
    print(i)
    bottom[i] += bottom[i+1]
    top[i] += top[i+1]
    print(bottom)
    print(top)

for i in range(H):
    res[i] = bottom[i] + top[-i-1]
    print(res)

answer = min(res)
print(answer, res.count(answer))
import sys
input = sys.stdin.readline

def calc(x,y,symbol):
    if symbol == '+':
        return x + y
    elif symbol == '-':
        return x - y
    else:
        return x * y

N = int(input())
prob = list(map(str,input().rstrip()))
count = N//2+1
dp = [[[0,0] for _ in range(count)] for _ in range(count)]
sym = []
for i in range(N):
    if i%2 == 0:
        dp[i//2][i//2] = [int(prob[i]),int(prob[i])]
    else:
        sym.append(prob[i])  
    
tmp = 1
for i in range(count-1,0,-1):
    for j in range(i):
        res = []
        for k in range(j,j+tmp):
            res.append(calc(dp[j][k][0],dp[k+1][j+tmp][0],sym[k]))
            res.append(calc(dp[j][k][1],dp[k+1][j+tmp][1],sym[k]))
            res.append(calc(dp[j][k][0],dp[k+1][j+tmp][1],sym[k]))
            res.append(calc(dp[j][k][1],dp[k+1][j+tmp][0],sym[k]))
        dp[j][j+tmp] = [max(res),min(res)]
    tmp += 1
print(dp[0][count-1][0])
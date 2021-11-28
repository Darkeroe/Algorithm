import sys
input = sys.stdin.readline

def check(start,end):
    if dp[start][end] != -1:
        return dp[start][end]
    
    tmp = 0
    if (DNA[start] == 'a' and DNA[end] == 't') or (DNA[start] == 'g' and DNA[end] == 'c'):
        tmp = check(start+1,end-1) + 2
        
    for i in range(start,end):
        tmp = max(tmp, check(start,i) + check(i+1,end))
    dp[start][end] = tmp
    
    return tmp

DNA = list(str(input().rstrip()))
length = len(DNA)
dp = [[-1 for _ in range(length)] for _ in range(length)]
check(0,length-1)

print(dp[0][length-1])
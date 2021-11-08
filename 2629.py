import sys
input = sys.stdin.readline

def dp(cnt,Wcnt):
    if cnt > N or Wcnt > sum_weight or arr[cnt][Wcnt]:
        return 0
    arr[cnt][Wcnt] = True
    ans[Wcnt] = True
    if cnt != N:
        dp(cnt+1,Wcnt+weight[cnt])
        dp(cnt+1,Wcnt)
        dp(cnt+1,abs(Wcnt-weight[cnt]))

N = int(input())
weight = list(map(int,input().split()))
T = int(input())
marble = list(map(int,input().split()))

sum_weight = sum(weight)
arr = [[False for _ in range(sum_weight+1)] for _ in range(N+1)]
ans = [False for _ in range(sum_weight+1)]
dp(0,0)

for i in marble:
    if i <= sum_weight and ans[i]:
        print('Y', end = ' ')
    else:
        print('N', end = ' ')
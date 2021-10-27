import sys
input = sys.stdin.readline

N,K = map(int,input().split())

tmp,digit,cnt = N,10**len(str(N)),1
arr = {}
for i in range(K):
    remain = tmp % K
    if remain == 0:
        print(cnt)
        break
    elif remain in arr or i == K-1:
        print(-1)
        break
    arr[remain] = 1 
    tmp = remain*digit+N
    cnt +=1
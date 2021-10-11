import sys
input = sys.stdin.readline

def find(start,end):
    global arr,ans
    tmp,idx,flag = 100,0,False
    for i in range(start,end):
        if ord(N[i]) < tmp and arr[i] != N[i]:
            flag = True
            tmp,idx = ord(N[i]),i
    if flag:
        arr[idx] = N[idx]
        ans = (''.join(arr))
        print(ans.replace('0',''))
        find(idx,end)
        find(start,idx)

N = list(input().strip())
arr = ['0' for _ in range(len(N))]
ans,length= '',len(N)
find(0,length)
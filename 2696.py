from heapq import heappop, heappush
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    ans = []
    M = int(input())//10+1
    arr,heap1,heap2 = [],[],[]
    for _ in range(M):
        arr += list(map(int,input().split()))
    if len(arr) == 1:
        ans.append(arr[0])
    else:
        if arr[0] < arr[1]:
            heappush(heap1,(-arr[0],arr[0]))
            heappush(heap2,arr[1])
        else:
            heappush(heap1,(-arr[1],arr[1]))
            heappush(heap2,arr[0])
        ans.append(arr[0])
    
    for target in arr[2:]:
        left, right = heap1[0][1], heap2[0]
        if target > right:
            heappush(heap2,target)
        else:
            heappush(heap1,(-target,target))
        
        if len(heap2) > len(heap1):
            tmp = heappop(heap2)
            heappush(heap1,(-tmp,tmp))
            ans.append(tmp)
        elif len(heap1)-1 == len(heap2):
            ans.append(heap1[0][1])
        elif len(heap1)-2 == len(heap2):
            tmp = heappop(heap1)[1]
            heappush(heap2,tmp)
    print(len(ans))
    length = len(ans)//10+1
    for i in range(length):
        print(*ans[i*10:(i+1)*10])
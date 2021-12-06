import sys
input = sys.stdin.readline

N,K = map(int,input().split())
order = list(map(int,input().split()))
tap = []
cnt = 0
for idx in range(K):
    tmp,flag = [],True
    if order[idx] in tap:
        continue
    elif len(tap) < N:
        tap.append(order[idx])
        continue
    else:    
        for plugged_device in tap:
            if plugged_device in order[idx:]:
                tmp.append(order[idx:].index(plugged_device))
            else:
                tmp.append(101)
                flag = False
                break
    delete = tmp.index(max(tmp))
    del tap[delete]
    tap.append(order[idx])
    cnt += 1

print(cnt)
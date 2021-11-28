import sys
input = sys.stdin.readline

def check(length,tree,cnt):
    prior,prefix_sum,left = tree,0,0
    for idx in range(K-1,-1,-1):
        if prior-chances[idx]+prefix_sum > length:
            if idx == K-1 or cnt-1 < 0:
                return False, 0
            else:
                cnt -= 1
                left = prior
                prefix_sum = prior-chances[idx]
                prior = chances[idx]
                if prefix_sum > length:
                    return False, 0
        else:
            prefix_sum += prior-chances[idx]
            prior = chances[idx]
    if prior > length:
        return False, 0
    if cnt > 0:
        left = chances[1]
    return True, left

ans = []
L,K,C = map(int,input().split())
chances = [0] + list(set(map(int,input().split())))
chances = list(chances)
chances.sort()
min_length,max_length = 1,L
K = len(chances)

while min_length <= max_length:
    mid = (min_length+max_length)//2
    flag, left = check(mid,L,C)
    if flag:
        max_length = mid - 1
        ans.append([mid,left])
    else:
        min_length = mid + 1

print(*min(ans))
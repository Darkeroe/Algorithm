from heapq import heappush,heappop,heapify
import sys
input = sys.stdin.readline
mod = 1000000007

T = int(input())
for _ in range(T):
    N = int(input())
    slime_list = list(map(int,input().split()))
    heapify(slime_list)
    
    ans = 1
    while len(slime_list) > 1:
        slime1 = heappop(slime_list)
        slime2 = heappop(slime_list)
        merged_slime = slime1*slime2
        heappush(slime_list,merged_slime)
        ans *= merged_slime
    
    print(ans%mod)        
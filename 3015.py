from collections import deque
import sys
input = sys.stdin.readline

ans,cnt = 0,1
queue = deque()
N = int(input())
for _ in range(N):
    queue.append(int(input()))
for i in queue:
    
    
print(ans)
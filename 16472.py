from collections import deque

N = int(input())
lang = str(input())
ans,res = 1,1
left, right = 0, 0
arr = deque()
alpha = [0 for _ in range(26)]
alpha[ord(lang[0])-97] += 1
arr.append(ord(lang[0])-97)
r = 0
while left <= right:
    right += 1
    if right >= len(lang):
        break
    alpha[ord(lang[right])-97] += 1
    arr.append(ord(lang[right])-97)
    res += 1
    if alpha[ord(lang[right])-97] == 1:
        ans += 1
    while ans > N:
        tmp = arr.popleft()
        res -= 1
        alpha[tmp] -= 1
        left += 1
        if alpha[tmp] == 0:
            ans -= 1
    if res >= r:
        r = res
print(r)
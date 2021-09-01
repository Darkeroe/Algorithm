
# def greedy(a,b,comp,tmp):
#     global flag
#     # print('comp',comp)
#     for i in range(a):
#         # print('i',i,comp)
#         if b[i] <= comp:
#             if i == len(b)-1:
#                 # print(tmp, b[i])
#                 tmp -= b[i]
#                 if tmp ==0:
#                     break
#                 else:
#                     flag = 1
#                     break
#             elif i != a-1:
#                 tmp -= b[i]
#                 if tmp == 0:
#                     break
#                 elif tmp > 0:
#                     greedy(a,b[(i+1):],tmp,tmp)
#                 else:
#                     tmp += b[i]

# a = int(input())
# b = list(map(int,input().split()))
# b.sort(reverse=True)
# comp = 0
# tmp = 0
# flag = 0
# while True:
#     comp += 1
#     tmp += 1
#     greedy(a,b,comp,tmp)
#     if flag == 1:
#         print(comp)
#         break

a=int(input())
b=list(map(int,input().split()))

b.sort()
target=1
for i in b:
    if target<i:
        break
    target+=i

print(target)

a = int(input())
b = [list(map(int,input().split())) for _ in range(a)]
b.sort(key=lambda x:-x[0])
arr= [0]*b[0][0]
b.sort(key=lambda x:(-x[1]))
result = 0
for i in range(a):
    for j in range(b[i][0]-1,-1,-1):
        if arr[j] == 0:
            arr[j] = 1
            result += b[i][1]
            break
print(result)

import collections
a,b = map(int,input().split())
c = list(input())
deq = collections.deque()
cnt = 0
dup = 0
for i in range(a):
    if cnt == b or i ==a-1:
        cnt = i
        break
    if int(c[i]) < int(c[i+1]):
        cnt += 1
    elif int(c[i]) == int(c[i+1]):
        for j in range(a-i-2):
            if int(c[i]) > int(c[i+2+j]):
                for k in range(j):
                    deq.append(c[i])
                i += j+1
                break
            elif int(c[i]) < int(c[i+2+j]):
                for k in range(j+2-(b-cnt)):
                    deq.append(c[i])
                dup += b-cnt
                cnt += b-cnt
                
                print('ooo',b,cnt,dup)
                i += j+2
                break
    else:
        deq.append(c[i])
print('sss',deq)
print(cnt,dup)
for i in range(a-cnt-dup):
    deq.append(c[cnt+i+dup])
    print('s',deq)
for i in range(a-b):
    print(deq.popleft(), end='')    

# print(c) 

# 1654551981


# a, b = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# res = 0
# for i in range(N):
#     pre = arr[i][0]
#     cnt = 1
#     for j in range(1,a):
#         if arr[i][j] == pre:
#             cnt += 1
#             pre = arr[i][j]
#         elif arr[i][j] == pre+1 and cnt >= 0:
#             if cnt >= b:
#                 cnt = 1
#                 pre = arr[i][j]
#             else:
#                 break
#         elif arr[i][j] == pre-1 and cnt >= 0:
#             cnt = - b + 1
#             pre = arr[i][j]
#         else:
#             break
#     else:
#         if cnt >= 0:
#             res += 1
 
# for j in range(a):
#     pre = arr[0][j]
#     cnt = 1
#     for i in range(1,a):
#         if arr[i][j] == pre:
#             cnt += 1
#             pre = arr[i][j]
#         elif arr[i][j] == pre+1 and cnt >= 0:
#             if cnt >= b:
#                 cnt = 1
#                 pre = arr[i][j]
#             else:
#                 break
#         elif arr[i][j] == pre-1 and cnt >= 0:
#             cnt = - b + 1
#             pre = arr[i][j]
#         else:
#             break
#     else:
#         if cnt >= 0:
#             res += 1
 
# print(res)
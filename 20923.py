import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
do, su, rnd = deque(), deque(), 0
do_gr, su_gr, target = deque(), deque(), 5
for _ in range(N):
    a, b = map(int,sys.stdin.readline().split())
    do.append(a)
    su.append(b)

def refresh():
    global do_gr, su_gr, target
    do_gr, su_gr, target= deque(), deque(), 5

def merge(case):
    global su, do
    if case == 1:
        for i in su_gr:
            do.appendleft(i)
        for i in do_gr:
            do.appendleft(i)
    else:
        for i in do_gr:
            su.appendleft(i)
        for i in su_gr:
            su.appendleft(i)

def dual(case):
    global target
    if case == 1:
        tmp = do.pop()
        do_gr.append(tmp)
        if len(do) == 0:
            print('su')
            exit()
    else:
        tmp = su.pop()
        su_gr.append(tmp)
        if len(su) == 0:
            print('do')
            exit()
    if tmp == 5:
        merge(1)
        refresh()
    elif target != 5 and tmp == target:
        merge(2)
        refresh()
    else:
        target = 5 - tmp

while rnd < M:
    dual(1)
    rnd += 1
    if rnd >= M:
        break
    dual(2)
    rnd += 1

if len(do) > len(su):
    print('do')
elif len(do) < len(su):
    print('su')
else:
    print('dosu')
import sys
input = sys.stdin.readline

def ccw(a,b,c,d,e,f):
    return (a*d+c*f+e*b) - (c*b+e*d+a*f)

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

res1 = ccw(x1,y1,x2,y2,x3,y3)
res2 = ccw(x1,y1,x2,y2,x4,y4)
res3 = ccw(x3,y3,x4,y4,x1,y1)
res4 = ccw(x3,y3,x4,y4,x2,y2)

if res1*res2==0 and res3*res4==0:
    if min(x1,x2) <= max(x3,x4) and max(x1,x2) >= min(x3,x4) and min(y1,y2) <= max(y3,y4) and min(y3,y4) <= max(y2,y1):
        print(1)
    else:
        print(0)
elif res1*res2<=0 and res3*res4<=0:
    print(1)
else:
    print(0)
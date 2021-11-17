import sys
input = sys.stdin.readline

def ccw(a,b,c,d,e,f,g,h):
    a1 = (a*d+c*f+e*b) - (c*b+e*d+a*f)
    a2 = (a*d+c*h+g*b) - (c*b+g*d+a*h)
    a3 = (e*h+g*b+a*f) - (g*f+a*h+e*b)
    a4 = (e*h+g*d+c*f) - (g*f+c*h+e*d)
    if a1*a2 <= 0 and a3*a4 <= 0:
        if ((a<e and a<g and c<e and c<g) or (e<a and e<c and g<a and g<c)):
            return False
        if ((b<f and b<h and d<g and d<h) or (f<b and f<d and h<b and h<d)):
            return False
        return True
    return False

T = int(input())
for _ in range(T):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int,input().split())
    x5,y5,x6,y6 = x3,y4,x4,y3
    if ccw(x1,y1,x2,y2,x3,y3,x5,y5) or ccw(x1,y1,x2,y2,x4,y4,x5,y5) or ccw(x1,y1,x2,y2,x3,y3,x6,y6) or ccw(x1,y1,x2,y2,x4,y4,x6,y6):
        print("T")
    else:
        if(max(x3,x4)>x1 and max(x3,x4)>x2 and min(x3,x4)<x1 and min(x3,x4)<x2):
            print("T")
        else:
            print("F")
import sys
input = sys.stdin.readline

while True:
    flag = False
    try:
        x = int(input())
        n = int(input())
        lego = [int(input()) for _ in range(n)]
        
        x *= 10000000
        lego.sort()
        
        start = 0
        end = n-1
        
        while start < end:
            summation = lego[start] + lego[end]
            if summation == x:
                flag = True
                print('yes',lego[start],lego[end])
                break
            elif summation > x:
                end -= 1
            else:
                start += 1

        if not flag:
            print('danger')
            
    except:
        break
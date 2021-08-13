M, N = map(int,input().split())

if M == N:
    print(N*2-2)
    print(N-((N-1)//2),(N+1)//2)

elif M > N:
    print(2*N-1)
    if N%2 == 1:
        print(M-(N//2) ,N//2+1)
    else:
        print(1+N//2, (N-1)//2+1)

else:
    print(2*M-2)
    if M%2 == 1:
        print(M//2+1, N-(M//2))
    else:
        print(M-M//2+1,M//2)
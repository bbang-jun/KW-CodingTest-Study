N, M = map(int, input().split())

RiceCake = list(map(int,input().split()))
Max = max(RiceCake)

while True:
    Ans = 0
    Max-=1
    for i in range(N):
        #check every lenght compare to cutter
        if(RiceCake[i]>Max):
            Ans=Ans+(RiceCake[i]-Max)
        
    if(Ans>=M):
        break

print(Max)

#used Comparing value with Maximum cutter length